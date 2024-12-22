def compute_linear_function_test(): 
    results = []
    # test cases
    test_cases = [
        {
            'name': 'Case 1',
            'x': 0,
            'y': 20,
        },
        {
            'name': 'Case 2',
            'x': 5,
            'y': 45
        },
        {
            'name': 'Case 3',
            'x': 0.0005,
            'y': 5
        },
        {
            'name': 'Case 4',
            'x': -25,
            'y': -105
        }
    ]
    
    # test cases
    for case in test_cases:
        try:
            result = linear_function(case['x'])
            assert result == case['y'], f'{case["name"]}: Y should be {case["y"]} but got {result}'
            results.append({
                'name': case['name'],
                'input': 'X: ' + str(case['x']),
                'expected_output': str(case['y']),
                'stdout': f'Y computed as {str(case["y"])}',
                'stderr': '',
                'passed': True
            })
        except AssertionError as e:
            results.append({
                'name': case['name'],
                'input': 'X: ' + str(case['x']),
                'expected_output': str(case['y']),
                'stdout': str(e),
                'stderr': '',
                'passed': False
            })
        except Exception as e:
            results.append({
                'name': case['name'],
                'input': 'X: ' + str(case['x']),
                'expected_output': case['y'],
                'stdout': '',
                'stderr': f'Unexpected error: {str(e)}',
                'passed': False
            })
    
    return results

# Create a function that returns the value of Y given an input X
# if the function is detailed by this equation: Y = 5x + 20
# Slope = 5
# Y-intercept = 20
def linear_function(x):
    return 5 * x + 20


if __name__ == '__main__':
    print({
        'results': compute_linear_function_test()
    })




[
    "def compute_linear_function_test(): ",
    "    results= []",
    "    # test cases",
    "    test_cases = [",
    "        {",
    "            'name': 'Case 1',",
    "            'x': 0,",
    "            'y': 20,",
    "        },",
    "        {",
    "            'name': 'Case 2',",
    "            'x': 5,",
    "            'y': 45",
    "        },",
    "        {",
    "            'name': 'Case 3',",
    "            'x': 0.0005,",
    "            'y': 5",
    "        },",
    "        {",
    "            'name': 'Case 4',",
    "            'x': -25,",
    "            'y': -105",
    "        }",
    "    ]",
    "    ",
    "    # test cases",
    "    for case in test_cases:",
    "        try:",
    "            result = linear_function(case['x'])",
    "            assert result == case['y'], f\"{case['name']}: Y should be {case['y']} but got {result}\"",
    "            results.append({",
    "                'name': case['name'],",
    "                'input': 'X: ' + str(case['x']),",
    "                'expected_output': str(case['y']),",
    "                'stdout': f\"Y computed as {str(case['y'])}\",",
    "                'stderr': '',",
    "                'passed': True",
    "            })",
    "        except AssertionError as e:",
    "            results.append({",
    "                'name': case['name'],",
    "                'input': 'X: ' + str(case['x']),",
    "                'expected_output': str(case['y']),",
    "                'stdout': str(e),",
    "                'stderr': '',",
    "                'passed': False",
    "            })",
    "        except Exception as e:",
    "            results.append({",
    "                'name': case['name'],",
    "                'input': 'X: ' + str(case['x']),",
    "                'expected_output': case['y'],",
    "                'stdout': '',",
    "                'stderr': f\"Unexpected error: {str(e)}\",",
    "                'passed': False",
    "            })",
    "    ",
    "    return results",
    "",
    "#Create a function that return the value of Y given an input X",
    "#if the function is detailed by this equation: Y = 5x + 20",
    "#Slope = 5",
    "#Y-intercept = 20",
    "def linear_function(x):",
    "    return 5 * x + 20",
    "",
    "if __name__ == '__main__':",
    "   print({",
    "      'results': compute_linear_function_test()",
    "    })"
]
