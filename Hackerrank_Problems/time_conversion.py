def timeConversion(s):
    #covert to railway time
    result  = ''
    if s[-2:] == 'AM':
        if s[:2] == '12':
            result = '00' + s[2:-2]
        else:
            result = s[:-2]
    else:
        if s[:2] == '12':
            result = s[:-2]
        else:
            result = str(int(s[:2]) + 12) + s[2:8]
    return result
# Example usage:
input_time = "07:05:45PM"
converted_time = timeConversion(input_time)
print(converted_time)  # Output: "19:05:45"
        