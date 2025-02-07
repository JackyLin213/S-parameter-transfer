def sdd21_function(num_equations):
    # 驗證輸入是否為正整數
    if not isinstance(num_equations, int) or num_equations <= 0:
        print("請輸入正整數")
        return
    
    for i in range(num_equations):
        # 計算基礎數值
        base = 4 * i  # 每4個數字為一組
        
        # 如果是前兩組特殊情況
        if i == 0:
            print("SDD21 = 0.5*(S21-S23-S41+S43)")
        elif i == 1:
            print("SDD21 = 0.5*(S65-S67-S85+S87)")
        else:
            # 計算四個S參數的位置
            pos1 = (base + 2, base + 1)    
            pos2 = (base + 2, base + 3)    
            pos3 = (base + 4, base + 1)    
            pos4 = (base + 4, base + 3)    
            
            print(f"SDD21 = 0.5*(S({pos1[0]},{pos1[1]})-S({pos2[0]},{pos2[1]})-S({pos3[0]},{pos3[1]})+S({pos4[0]},{pos4[1]}))")

def sdd11_function(num_equations):
    # 驗證輸入是否為大於 0 的正整數
    if not isinstance(num_equations, int) or num_equations <= 0:
        print("請輸入大於 0 的正整數")
        return
    
    for i in range(num_equations):
        # 計算基礎數值
        base = 4 * i  # 每4個數字為一組
        
        # 如果是前兩組特殊情況
        if i == 0:
            print("SDD11 = 0.5*(S11-S13-S31+S33)")
        elif i == 1:
            print("SDD11 = 0.5*(S55-S57-S75+S77)")
        else:
            # 計算四個S參數的位置
            pos = base + 8  # 從9開始遞增
            print(f"SDD11 = 0.5*(S({pos+1},{pos+1})-S({pos+1},{pos+3})-S({pos+3},{pos+1})+S({pos+3},{pos+3}))")

# 主程式
while True:
    # 取得使用者想要計算的SDD類型
    sdd_type = input("請輸入要計算的類型 (輸入sdd11或sdd21，輸入exit結束程式): ").lower()
    
    # 檢查是否要結束程式
    if sdd_type == 'exit':
        print("程式結束")
        break
    
    # 檢查輸入是否有效
    if sdd_type not in ['sdd11', 'sdd21']:
        print("無效的輸入！請輸入sdd11或sdd21")
        continue
    
    # 取得要計算的組數 
    try:
        num = int(input("請輸入要計算的組數: "))
        
        # 根據選擇執行對應的函數
        if sdd_type == 'sdd21':
            sdd21_function(num)
        else:
            sdd11_function(num)
            
        print("\n")  # 新增空行，讓輸出更清楚
        
    except ValueError:
        print("請輸入有效的數字！\n")