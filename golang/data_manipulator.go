package main

import (
	"fmt"
	"os"
	"encoding/csv"
	"strconv"
)


func main(){
	
    records, err := importData("electric_vehicle.csv")
    if err != nil {
        fmt.Println("Error:", err)
        return
    }

    // // Print the records
    // for _, record := range records {
    //     fmt.Println(record)
    // }

	recordsMap, err := recordsToMap(records)
	if err != nil {
		fmt.Println(err)	
	}
	// fmt.Println(recordsMap)

	final, err := reduce(recordsMap)
	if err != nil {
		fmt.Println(err)	
	}
	
	for _, row := range final{
		fmt.Println(" ")
		fmt.Println(row["Model Year"])
		fmt.Println(row["Make"])
		fmt.Println(row["Model"])
		fmt.Println(row["VIN (1-10)"])
	}


	// get cars before 2019, make is not a Tesla, return their VIN and year, and make and model

}

func reduce(recordsMap []map[string]string)([]map[string]string, error){
	final := []map[string]string{}

	for _, record := range recordsMap {

		fmt.Println(record)
		if len(record["Model Year"]) == 0{
			fmt.Println(record["Year"])
			continue
		}

		year, err := strconv.Atoi(record["Model Year"])
		if err != nil {
			return nil, err
		}

		if year < 2019 && record["Make"] != "TESLA"{
			final = append(final, record)
		}
	}
	return final, nil
}

func recordsToMap(records [][]string)([]map[string]string, error){
	var recordsMap []map[string]string

	recordHeader := records[0]
	for i, record := range records {
		if i == 0{
			continue
		} else {

			if len(record) != len(recordHeader) {
				return nil, fmt.Errorf("record len is off")
			}

			row := make(map[string]string)

			for j, header := range recordHeader {
				row[header] = record[j]
			}
			recordsMap = append(recordsMap, row)

		}

	}
	return recordsMap, nil
}

func importData(filePath string)([][]string, error){
	file, err := os.Open(filePath)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	reader := csv.NewReader(file)

	records, err := reader.ReadAll()
	if err != nil {
		return nil, err
	}

	return records, nil
}