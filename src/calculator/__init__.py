import re

class Calculator:
    
    _NUM_NAMES = {
        # English
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        # German
        'null': 0, 'eins': 1, 'zwei': 2, 'drei': 3, 'vier': 4,
        'fuenf': 5, 'sechs': 6, 'sieben': 7, 'acht': 8, 'neun': 9,
        # Spanish
        'cero': 0, 'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4,
        'cinco': 5, 'seis': 6, 'siete': 7, 'ocho': 8, 'nueve': 9,
        # Russian
        'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4,
        'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9,
        # Chinese
        '零': 0, '一': 1, '二': 2, '三': 3, '四': 4,
        '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
    }

    # Mapping for Roman Numerals
    _ROMAN_MAP = {
        'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 
        'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10
    }

    def _to_number(self, val):
        """Converts an input (number, string, number-name, or Roman numeral) to a float or int."""
        if isinstance(val, (int, float)):
            return val

        if isinstance(val, str):
            s = val.strip()
            s_lower = s.lower()

            # 1. Check for number names
            if s_lower in self._NUM_NAMES:
                return self._NUM_NAMES[s_lower]

            # 2. Check for Roman Numerals - Case Sensitive
            s_upper = s.upper()
            if s_upper in self._ROMAN_MAP:
                return self._ROMAN_MAP[s_upper]
            
            # 3. Check for numerical string
            try:
                # Check if it's an integer string without decimal point
                if re.fullmatch(r'\d+', s):
                    return int(s)
                # Check if it's a float string
                return float(s)
            except ValueError:
                # If it's a string that's not a known name or number, treat it as 0 (or raise error)
                raise ValueError(f"Input '{val}' cannot be converted to a number.")
        
        # Fallback for unexpected types
        raise TypeError(f"Unsupported type for conversion: {type(val)}")

    def add(self, a, b):
        """Return the sum of a and b."""
        num_a = self._to_number(a)
        num_b = self._to_number(b)
        return num_a + num_b

    def sub(self, a, b):
        """Subtract b from a."""
        num_a = self._to_number(a)
        num_b = self._to_number(b)
        return num_a - num_b

    def mul(self, a, b):
        """Multiply a and b."""
        num_a = self._to_number(a)
        num_b = self._to_number(b)
        return num_a * num_b

    def div(self, a, b):
        """Divide a by b."""
        num_a = self._to_number(a)
        num_b = self._to_number(b)
        if num_b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num_a / num_b

    def factorize(self, n):
        """Return prime factors of n. Requires n to be a positive integer."""
        num_n = self._to_number(n)
        
        # Must be an integer for factorization
        if not isinstance(num_n, int) and num_n == int(num_n):
            num_n = int(num_n)
        
        if not isinstance(num_n, int):
            raise TypeError("Factorize argument must be an integer or convertible to an integer.")
        
        # *** ADDED CHECK FOR NEGATIVE NUMBERS ***
        if num_n < 0:
            raise ValueError("Factorize argument must be a positive integer")
        
        if num_n <= 1:
            return []
        
        factors = []
        d = 2
        temp_n = num_n
        while d * d <= temp_n:
            while temp_n % d == 0:
                factors.append(d)
                temp_n //= d
            d += 1
        if temp_n > 1:
            factors.append(temp_n)
            
        return factors