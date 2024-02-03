import pandas as pd

def excel_to_json(excel_file, json_file):
    # 读取Excel文件
    df = pd.read_excel(excel_file)
    
    # 处理合并单元格导致的null值问题，填充空值
    df = df.ffill()
    
    # 将DataFrame保存为JSON文件，设置orient为records
    df.to_json(json_file, orient='records', force_ascii=False)

if __name__ == "__main__":
    #xlsx后期修改
    excel_file_path = 'data.xlsx'  # 替换为你的Excel文件路径
    json_file_path = 'data.json'  # 替换为输出JSON文件路径

    excel_to_json(excel_file_path, json_file_path)






