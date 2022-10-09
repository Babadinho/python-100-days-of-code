# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.split()}

print(result)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:(weather*9/5)+32 for (day,weather) in weather_c.items()}

print(weather_f)

# Loop through pandas dataframe
# for (index, row) in pandas_dataframe.iterrows():
#     print(row)
#     print(row.item)
#     print(index)
