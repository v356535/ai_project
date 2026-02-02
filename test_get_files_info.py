from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def main():

	
	working_dir = "calculator"
	
	print(get_files_info(working_dir, "."))
	print(get_files_info(working_dir, "pkg"))
	print(get_files_info(working_dir, "/bin"))
	print(get_files_info(working_dir, "../"))

main()
