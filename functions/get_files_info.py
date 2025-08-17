def get_files_info(working_directory, directory="."):
    import os
    try:
        joined_path = os.path.join(working_directory, directory)
        abs_joined_path = os.path.abspath(joined_path)
        abs_working_dir = os.path.abspath(working_directory)

        if not abs_joined_path.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(abs_joined_path):
            return f'Error: "{directory}" is not a directory'

        file_list = []
        for file in os.listdir(joined_path):
            item_path = os.path.join(joined_path, file)
            file_list.append(
                f"- {file}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}"
            )
        return "\n".join(file_list)

    except Exception as e:
        return f"Error: {str(e)}"