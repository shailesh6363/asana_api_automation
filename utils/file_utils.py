from pathlib import Path
import pandas as pd
import json
import os
# This is the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# This is the directory where the test data is stored
WORKSPACE_TEST_DATA_DIR = BASE_DIR.joinpath('TestData')


def get_test_data_file(file_name):
    filePath=WORKSPACE_TEST_DATA_DIR.joinpath(file_name)


    return filePath


def nest_dict(flat_dict):
    """Converts a flat dictionary with dot-separated keys into a nested dictionary."""
    nested_dict = {}
    for key, value in flat_dict.items():
        keys = key.split(".")  # Split on dot notation
        temp = nested_dict
        for k in keys[:-1]:  # Traverse to the last nested level
            temp = temp.setdefault(k, {})
        temp[keys[-1]] = value  # Set the final value
    return nested_dict


def save_json_to_file(json_body, module_name, json_name):
    """Saves the JSON body to a file in the structured directory Requests/module_name/json_name.json"""
    dir_path = os.path.join("Requests", module_name)
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, f"{json_name}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(json_body, f, indent=4)
    return file_path


def get_test_case_data(excel_file, sheet_name, test_case_name=None, save_json=True, custom_json_updates=None):
    df = pd.read_excel(excel_file, sheet_name=sheet_name, engine="openpyxl").fillna("")

    # Normalize column names: Remove spaces & convert to lowercase
    df.columns = df.columns.str.strip().str.lower()

    test_cases = []
    for _, row in df.iterrows():
        # Extract payload and handle nested JSON keys
        json_body = {
            row[f"payloadkey{i}"]: row[f"payloadvalue{i}"]
            for i in range(1, 10)
            if pd.notna(row.get(f"payloadkey{i}")) and row[f"payloadkey{i}"]
        }
        json_body = nest_dict(json_body)  # Convert to nested JSON

        # Apply runtime custom updates to json_body
        if custom_json_updates:
            json_body.update(custom_json_updates)

        # Extract headers
        headers = {}
        if pd.notna(row.get("headers")) and row["headers"]:
            try:
                headers = json.loads(row["headers"])
            except json.JSONDecodeError:
                headers = {}

        test_case = {
            "test_case": row.get("testcase", ""),
            "url": row.get("url", ""),
            "endpoint": row.get("endpoint", ""),
            "method": row.get("method", "GET").upper(),
            "headers": headers,
            "json_body": json_body,
            "json_file_path": None
        }

        if save_json:
            module_name = row.get("module", "default_module")
            json_name = row.get("jsonname", "default_request")
            json_path = save_json_to_file(json_body, module_name, json_name)
            test_case["json_file_path"] = json_path

        test_cases.append(test_case)

    if test_case_name:
        filtered_test_cases = [tc for tc in test_cases if tc["test_case"] == test_case_name]
        return filtered_test_cases if filtered_test_cases else [{}]  # Ensure it returns a list

    return test_cases



t=get_test_case_data(get_test_data_file("test_data.xlsx"),sheet_name='workSpace_data',test_case_name="TC4",save_json=True)
print(t)