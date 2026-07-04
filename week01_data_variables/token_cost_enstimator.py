# ram >> 40
# sham >> 50

print("=== AI Token Cost Estimator ===")
tokens = int(input("How many tokens? ")) ## 1000
price_per_1000 = float(input("Price per 1000 tokens (in rupees)? ")) # 1 
cost = (tokens / 1000) * price_per_1000 
print(f"Estimated cost: ₹{cost:.2f}") #### 2.3445566