def sort(width, height, length, mass):
    """
    Sorts packages into appropriate stacks based on volume and mass criteria.
    
    Args:
        width (float): Package width in centimeters
        height (float): Package height in centimeters  
        length (float): Package length in centimeters
        mass (float): Package mass in kilograms
        
    Returns:
        str: Stack name where package should go ("STANDARD", "SPECIAL", or "REJECTED")
    """
    
    # Calculate volume
    volume = width * height * length
    
    # Check if package is bulky
    is_bulky = (volume >= 1_000_000 or 
                width >= 150 or 
                height >= 150 or 
                length >= 150)
    
    # Check if package is heavy
    is_heavy = mass >= 20
    
    # Determine stack based on criteria
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL" 
    else:
        return "STANDARD"


# Test cases to verify the implementation
def test_sort():
    """Test function with various package scenarios"""
    
    print("Testing package sorting function:")
    print("=" * 40)
    
    # Test cases: (width, height, length, mass, expected_result)
    test_cases = [
        # Standard packages
        (10, 10, 10, 5, "STANDARD"),
        (50, 50, 50, 10, "STANDARD"),
        
        # Bulky packages (volume >= 1,000,000)
        (100, 100, 100, 5, "SPECIAL"),  # Volume = 1,000,000
        (200, 100, 50, 10, "SPECIAL"),  # Volume = 1,000,000
        
        # Bulky packages (dimension >= 150)
        (150, 10, 10, 5, "SPECIAL"),
        (10, 150, 10, 5, "SPECIAL"), 
        (10, 10, 150, 5, "SPECIAL"),
        
        # Heavy packages
        (50, 50, 50, 20, "SPECIAL"),
        (10, 10, 10, 25, "SPECIAL"),
        
        # Rejected packages (both bulky and heavy)
        (150, 10, 10, 20, "REJECTED"),  # Bulky dimension + heavy
        (100, 100, 100, 25, "REJECTED"),  # Bulky volume + heavy
        (200, 10, 10, 30, "REJECTED"),  # Bulky dimension + heavy
    ]
    
    all_passed = True
    for width, height, length, mass, expected in test_cases:
        result = sort(width, height, length, mass)
        status = "✓" if result == expected else "✗"
        
        if result != expected:
            all_passed = False
            
        print(f"{status} Package ({width}×{height}×{length}, {mass}kg) → {result} (expected: {expected})")
    
    print("=" * 40)
    print(f"All tests passed: {all_passed}")
    return all_passed


if __name__ == "__main__":
    # Run tests
    test_sort()
    
    # Example usage
    print("\nExample usage:")
    print(f"sort(50, 50, 50, 10) = {sort(50, 50, 50, 10)}")
    print(f"sort(150, 20, 20, 15) = {sort(150, 20, 20, 15)}")
    print(f"sort(100, 100, 100, 25) = {sort(100, 100, 100, 25)}")