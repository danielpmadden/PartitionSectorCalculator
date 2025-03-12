def bytes_to_sectors(size_mb):
    """
    Convert size in megabytes to the number of sectors.
    
    :param size_mb: Size in MB.
    :type size_mb: int or float
    :return: The number of sectors.
    :rtype: int
    """
    if size_mb <= 0:
        raise ValueError("Partition size must be greater than 0.")
    
    # 1 MB = 1024 * 1024 bytes; 1 sector = 512 bytes
    return size_mb * 1024 * 1024 // 512

def get_valid_integer(prompt_text):
    """
    Get a valid positive integer from user.
    
    :param prompt_text: The text prompt for user input.
    :type prompt_text: str
    :return: Validated integer input.
    :rtype: int
    """
    while True:
        try:
            value = int(input(prompt_text))
            if value < 0:
                print("Error: Enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_partition(starting_sector, size_mb):
    """
    Calculate first and last sector for a given partition size.
    
    :param starting_sector: The sector where the partition starts.
    :param size_mb: The partition size in MB.
    :return: Tuple of (first sector, last sector).
    :rtype: tuple(int, int)
    """
    total_sectors = bytes_to_sectors(size_mb)
    return starting_sector, starting_sector + total_sectors - 1

def main():
    """
    Main function to get user input and display partition details.
    """
    starting_sector = get_valid_integer("Enter the starting sector: ")
    size_mb = get_valid_integer("Enter the partition size in MB: ")

    try:
        first_sector, last_sector = calculate_partition(starting_sector, size_mb)

        print(f"\nPartition Details:")
        print(f"Starting from sector: {starting_sector}")
        print(f"Size: {size_mb}MB")
        print(f"First sector: {first_sector}")
        print(f"Last sector: {last_sector}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
