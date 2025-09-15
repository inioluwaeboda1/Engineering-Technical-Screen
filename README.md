# Package Sorting System for Thoughtful's Robotic Automation Factory

## Overview

This repository contains a package sorting function designed for Thoughtful's robotic automation factory. The function automatically dispatches packages to the correct stack based on their volume and mass characteristics.

## Problem Description

The robotic arm needs to sort packages into three different stacks:

- **STANDARD**: Packages that are neither bulky nor heavy
- **SPECIAL**: Packages that are either bulky OR heavy (but not both)
- **REJECTED**: Packages that are BOTH bulky AND heavy

### Classification Rules

**Bulky Package**: A package is considered bulky if:
- Its volume (Width × Height × Length) ≥ 1,000,000 cm³, OR
- Any dimension (width, height, or length) ≥ 150 cm

**Heavy Package**: A package is considered heavy if:
- Its mass ≥ 20 kg

## Implementation

### Function Signature
```python
def sort(width, height, length, mass) -> str
```

**Parameters:**
- `width` (float): Package width in centimeters
- `height` (float): Package height in centimeters
- `length` (float): Package length in centimeters
- `mass` (float): Package mass in kilograms

**Returns:**
- `str`: Stack name ("STANDARD", "SPECIAL", or "REJECTED")

### Algorithm Logic

1. Calculate the package volume: `volume = width × height × length`
2. Check if bulky: `volume ≥ 1,000,000` OR any dimension `≥ 150`
3. Check if heavy: `mass ≥ 20`
4. Apply sorting rules:
   - If bulky AND heavy → "REJECTED"
   - If bulky OR heavy → "SPECIAL"
   - Otherwise → "STANDARD"

## Usage

### Running the Code

```bash
python package_sorter.py
```

### Example Usage

```python
from package_sorter import sort

# Standard package
result = sort(50, 50, 50, 10)  # Returns "STANDARD"

# Bulky package (large dimension)
result = sort(150, 20, 20, 15)  # Returns "SPECIAL"

# Heavy package
result = sort(50, 50, 50, 25)  # Returns "SPECIAL"

# Rejected package (both bulky and heavy)
result = sort(100, 100, 100, 25)  # Returns "REJECTED"
```

## Test Cases

The implementation includes comprehensive test cases covering:

- **Standard packages**: Small dimensions and light weight
- **Bulky packages**: Both volume-based (≥1M cm³) and dimension-based (≥150 cm)
- **Heavy packages**: Mass ≥ 20 kg
- **Rejected packages**: Various combinations of bulky and heavy criteria

### Running Tests

The test suite runs automatically when executing the main script:

```bash
python package_sorter.py
```

Expected output:
```
Testing package sorting function:
========================================
✓ Package (10×10×10, 5kg) → STANDARD (expected: STANDARD)
✓ Package (50×50×50, 10kg) → STANDARD (expected: STANDARD)
✓ Package (100×100×100, 5kg) → SPECIAL (expected: SPECIAL)
...
========================================
All tests passed: True
```

## File Structure

```
package-sorter/
│
├── README.md           # This file
├── package_sorter.py   # Main implementation
└── requirements.txt    # Python dependencies (if any)
```

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Time Complexity

- **Time Complexity**: O(1) - Constant time operations
- **Space Complexity**: O(1) - Constant space usage

## Edge Cases Handled

- Packages exactly at threshold values (volume = 1,000,000 cm³, mass = 20 kg, dimension = 150 cm)
- Various combinations of bulky criteria (volume vs dimension)
- Floating-point inputs for dimensions and mass

## Author

Created as part of Thoughtful's robotic automation factory challenge.

## License

This project is provided as-is for evaluation purposes.