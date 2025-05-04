import re

# Function to extract and format numbers for LaTeX

def extract_and_format_for_latex(log_line):
    # Find all occurrences of | ... |
    matches = re.findall(r'\| ([\d.]+) ([\d.]+) \|', log_line)
    
    # Extract the second number from each match
    second_numbers = [match[1] for match in matches]
    
    # Join the numbers with & for LaTeX
    latex_formatted = ' & '.join(second_numbers)
    
    return latex_formatted

# Example log line
log_line = "0.0022 348.8337 | 0.0023 352.5468 | 0.0023 352.8061 | 0.0025 342.9573 | 0.0124 0.3388 | Time: 273.3017 | VAL: 0.2633 0.5460 | 0.0217 0.8168 | 0.2644 233.1953 | 0.0684 251.5249 | 0.0008 4.5462 | 0.0004 13.2385 | 0.0015 282.4872 | 0.0015 285.5425 | 0.0016 285.6265 | 0.0017 283.2442 | 0.0070 0.2629 | Time: 2.4238 | TEST: 0.2674 0.5393 | 0.0228 0.8257 | 0.2676 234.0935 | 0.0684 249.6690 | 0.0005 4.4940 | 0.0004 13.0797 | 0.0015 282.3926 | 0.0016 286.6886 | 0.0016 285.0395 | 0.0018 284.4034 | 0.0074 0.2671"

# Get the LaTeX formatted string
latex_string = extract_and_format_for_latex(log_line)

# Print the result
print(latex_string) 