"""
合并多个Excel文件的简单示例
"""
import pandas as pd
import os


def merge_excel_files(folder_path, output_file="merged.xlsx"):
    """合并指定文件夹下所有.xlsx文件"""
    all_data = []
    for file in os.listdir(folder_path):
        if file.endswith('.xlsx'):
            file_path = os.path.join(folder_path, file)
            df = pd.read_excel(file_path)
            all_data.append(df)
            print(f"已读取: {file}")

    if all_data:
        result = pd.concat(all_data, ignore_index=True)
        result.to_excel(output_file, index=False)
        print(f"合并完成！结果已保存为: {output_file}")
        return True
    else:
        print("未找到.xlsx文件")
        return False


if __name__ == "__main__":
    # 使用示例
    merge_excel_files("./excels")  # 合并当前目录下excels文件夹里的所有Excel