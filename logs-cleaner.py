#logs-cleaner for YARD logs

def filter_only_message(file_name):
    seen_lines = set()  # To keep track of unique lines
    
    with open(file_name, 'r') as original_file, open('filtered_error.log', 'w') as filtered_file:
        for line in original_file:
            # find the index of the fourth occurrence of ']'
            fourth_bracket_index = line.find(']', line.find(']', line.find(']', line.find(']') + 1) + 1) + 1) + 1 
            # slice the line to remove occurrences of '[some info]'
            modified_line = line[fourth_bracket_index:]
            
            # Check if the modified line is not already seen
            if modified_line not in seen_lines:
                # Write the modified line to the filtered log file
                filtered_file.write(modified_line)
                
                # Add the modified line to the set of seen lines
                seen_lines.add(modified_line)



def main():
    filter_only_message('errorlog.log')
    
main()