def compute_linear_function_test():
    results = []
    
    # test cases
    test_cases = [
        {
            "name": "Case 1",
            "x": np.array([5, 10, 15, 20]),
            "y": np.array([15, 25, 30, 35]),
            "initial_w": 2,
            "initial_b": 3,
            "expected_output": 10.125
        },
        {
            "name": "Case 2",
            "x": np.array([5, 10, 15, 20]),
            "y": np.array([15, 25, 30, 35]),
            "initial_w": 2,
            "initial_b": 1,
            "expected_cost": 8.625
        },
        {
            "name": "Case 3",
            "x": np.array([1.5, 3, 4.5, 6, 7.5]),
            "y": np.array([9, 12, 15, 18, 21]),
            "initial_w": 1,
            "initial_b": 0,
            "expected_cost": 57.375
        },
        {
            "name": "Case 4",
            "x": np.array([1.5, 3, 4.5, 6, 7.5]),
            "y": np.array([9, 12, 15, 18, 21]),
            "initial_w": 1,
            "initial_b": 1,
            "expected_cost": 47.375
        },
        {
            "name": "Case 5",
            "x": np.array([1.5, 3, 4.5, 6, 7.5]),
            "y": np.array([7, 10, 13, 15, 19]),
            "initial_w": 1,
            "initial_b": 0,
            "expected_cost": 36.475
        }
    ]
    
    # test cases
    for case in test_cases:
        try:
            cost = compute_cost(case["x"], case["y"], case["initial_w"], case["initial_b"])
            assert np.isclose(cost, case["expected_cost"]), f"{case['name']}: Cost should be close to {case['expected_cost']} but got {cost}"
            results.append({
                "name": case["name"],
                "input": "X: " + str(case["x"].tolist()) + "\nY: " + str(case["y"].tolist()) + "\nInital_w: " + str(case["initial_w"]) + "\nInitial_b: " + str(case["initial_b"]),
                "expected_output": case["expected_cost"],
                "stdout": f"Cost computed as {cost}",
                "stderr": "",
                "passed": True
            })
        except AssertionError as e:
            results.append({
                "name": case["name"],
                "input": {
                    "x": case["x"].tolist(),
                    "y": case["y"].tolist(),
                    "initial_w": case["initial_w"],
                    "initial_b": case["initial_b"]
                },
                "expected_output": case["expected_cost"],
                "stdout": str(e),
                "stderr": "",
                "passed": False
            })
        except Exception as e:
            results.append({
                "name": case["name"],
                "input": {
                    "x": case["x"].tolist(),
                    "y": case["y"].tolist(),
                    "initial_w": case["initial_w"],
                    "initial_b": case["initial_b"]
                },
                "expected_output": case["expected_cost"],
                "stdout": "",
                "stderr": f"Unexpected error: {str(e)}",
                "passed": False
            })
    
    return results

#Create a function that return the value of Y given an input X
#if the function is detailed by this equation: Y = 5x + 20
#Slope = 5
#Y-intercept = 20
def linear_function(x):
    return


if __name__ == '__main__':
   print({
      "results": compute_tests()
    })