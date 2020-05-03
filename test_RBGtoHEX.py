import RBGtoHEX as rgb

# ------------------------------------------------------------------------------------------------------------------
# check for when red are out of the range 0-255, testing rounder
r = -5
g = 124
b = 35
result = rgb.rgb(r, g, b)
expected = "007C23"
reason = "The rounder function is not work properly for red"

if result != expected:
    print("Test Failed: Received", result, 'Expected', expected, "--\n", reason)
    print()
# ------------------------------------------------------------------------------------------------------------------
# check for when green are out of the range 0-255, testing rounder
r = 5
g = 1124
b = 35
result = rgb.rgb(r, g, b)
expected = "05FF23"
reason = "The rounder function is not work properly for green"

if result != expected:
    print("Test Failed: Received", result, 'Expected', expected, "--\n", reason)
    print()
# ------------------------------------------------------------------------------------------------------------------
# check for when blue are out of the range 0-255, testing rounder
r = 5
g = 124
b = -35
result = rgb.rgb(r, g, b)
expected = "057C00"
reason = "The rounder function is not work properly for blue"

if result != expected:
    print("Test Failed: Received", result, 'Expected', expected, "--\n", reason)
    print()
# ------------------------------------------------------------------------------------------------------------------
# check for proper conversion, test 1
r = 255
g = 255
b = 255
result = rgb.rgb(r, g, b)
expected = "FFFFFF"
reason = "The rgb_helper or the converter could be at fault, test 1"

if reason != expected:
    print("Test Failed: Received", result, 'Expected', expected, "--\n", reason)
    print()
# ------------------------------------------------------------------------------------------------------------------
# check for proper conversion, test 2
r = 255
g = 255
b = 300
result = rgb.rgb(r, g, b)
expected = "FFFFFF"
reason = "The rgb_helper or the converter could be at fault, test 2"

if reason != expected:
    print("Test Failed: Received", result, 'Expected', expected, "--\n", reason)
    print()
# ------------------------------------------------------------------------------------------------------------------
# check for proper conversion, test 3
r = 0
g = 0
b = 0
result = rgb.rgb(r, g, b)
expected = "000000"
reason = "The rgb_helper or the converter could be at fault, test 3"

if reason != expected:
    print("Test Failed: Received", result, 'Expected', expected, "--\n", reason)
    print()
# ------------------------------------------------------------------------------------------------------------------
# check for proper conversion, test 4
r = 148
g = 0
b = 211
result = rgb.rgb(r, g, b)
expected = "9400D3"
reason = "The rgb_helper or the converter could be at fault, test 4"

if reason != expected:
    print("Test Failed: Received", result, 'Expected', expected, "--\n", reason)
    print()
