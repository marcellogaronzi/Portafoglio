import json
import scripts.csv_to_dict as csvConverter

def dict_to_json():
    with open("out/result.json", 'w', newline="\n") as json_outputFile:
            json_outputFile.write(json.dumps(csvConverter.csv_to_dict(), indent=4))

def main():
    dict_to_json()



if __name__ == "__main__":
    main()