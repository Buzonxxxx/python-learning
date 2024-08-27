import itertools

def pairwise_combinations(parameters):
    pairs = []
    for param1, param2 in itertools.combinations(parameters.keys(), 2):
        for val1 in parameters[param1]:
            for val2 in parameters[param2]:
                pairs.append({param1: val1, param2: val2})
    return pairs

# 測試參數
parameters = {
    "browser": ["Chrome", "Firefox", "Safari"],
    "os": ["Windows", "MacOS", "Linux"],
    "resolution": ["1080p", "4K", "8K"]
}

# 生成 pairwise 組合
test_cases = pairwise_combinations(parameters)

# 打印測試用例
for i, test_case in enumerate(test_cases, 1):
    print(f"Test Case {i}: {test_case}")

print(f"\nTotal test cases: {len(test_cases)}")