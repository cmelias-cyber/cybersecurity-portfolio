# File Permissions in Linux

## Project Description (Executive Summary)

The purpose of this project was to examine and update Linux file and directory permissions to ensure that system authorization matched organizational security requirements. I reviewed the permissions assigned to the user, group, and other users to verify that they matched the organization's authorization requirements and security policies.

I then used the `chmod` command to remove unauthorized access, secure an archived hidden file, and ensure that only the file owner could access a sensitive directory. These changes applied the principle of least privilege and helped protect the organization’s research data.

## Check File and Directory Details

To examine the permissions of all files and directories in the `/home/researcher2/projects` directory, I used the following command:

```bash
ls -la
```

The `ls` command lists the contents of a directory. The `-l` option displays detailed information, including file permissions, ownership, file size, and modification dates. The `-a` option includes hidden files, whose names begin with a period.

The `ls -la` command displayed a detailed listing of the directory contents. The first column of the output contains a 10-character permission string for each file and directory, followed by the file or directory name.

```text
-rw-rw-rw- project_k.txt
-rw-r----- project_m.txt
-rw-rw-r-- project_r.txt
-rw-rw-r-- project_t.txt
-rw--w---- .project_x.txt
drwx--x--- drafts
```
The output also includes the current directory (`.`) and the parent directory (`..`), which are displayed because of the `-a` option. These entries help identify the current location within the file system while ensuring that hidden files are also listed. The directory contains five project files, one hidden file (`.project_x.txt`), and one subdirectory (`drafts`).

> Add a screenshot of the `ls -la` command and its output here if available.

## Describe the Permissions String

Linux represents permissions using a 10-character string. For example:

```text
-rw-rw-rw-
```

This permission string belongs to `project_k.txt`.

The first character identifies the file type:

* `-` indicates a regular file.
* `d` would indicate a directory.

The remaining nine characters are divided into three groups:

```text
rw- rw- rw-
```

The first group represents the permissions assigned to the file owner, the second group represents the file's assigned group, and the third group represents all other users on the system.

Each group can contain the following characters:

* `r` means read permission.
* `w` means write permission.
* `x` means execute permission.
* `-` means the permission has not been granted.

For `project_k.txt`, the owner, group, and other users all had read and write permissions. This did not meet the organization’s requirement because other users were not permitted to write to files.

## Change File Permissions

The organization does not allow other users to have write access to any files. The permission string for `project_k.txt` was:

```text
-rw-rw-rw-
```

The final `rw-` showed that other users had both read and write access. I removed write permission from other users with the following command:

```bash
chmod o-w project_k.txt
```

In this command:

* `chmod` changes file or directory permissions.
* `o` represents other users.
* `-` removes a permission.
* `w` represents write permission.
* `project_k.txt` identifies the file being modified.

After running the command, I used `ls -l project_k.txt` to verify the change:

```bash
ls -l project_k.txt
```

The updated permission string was:

```text
-rw-rw-r--
```

The owner and group retained read and write permissions, while other users retained only read permission. Other users could no longer modify the file.

> Add a screenshot of the `chmod o-w project_k.txt` command and verification output here if available.

## Change File Permissions on a Hidden File

The file `.project_x.txt` is hidden because its name begins with a period. Hidden files are not displayed by a standard `ls` command, but they are displayed when the `-a` option is used.

The file originally had the following permissions:

```text
-rw--w----
```

These permissions allowed the owner to read and write to the file. The group could write to it but could not read it. The organization required the archived file to be readable by the owner and group, with no write permissions assigned to anyone.

I used the following command:

```bash
chmod u-w,g-w,g+r .project_x.txt
```

In this command:

* `u-w` removes write permission from the user.
* `g-w` removes write permission from the group.
* `g+r` adds read permission for the group.
* `.project_x.txt` identifies the hidden file being modified.

I then verified the permissions with:

```bash
ls -la .project_x.txt
```

The updated permission string was:

```text
-r--r-----
```

The owner and group could read the archived file, but no user had write permission. Other users had no access.

> Add a screenshot of the hidden-file permission command and its output here if available.

## Change Directory Permissions

The `drafts` directory originally had the following permission string:

```text
drwx--x---
```

The first character, `d`, identifies it as a directory. The owner had read, write, and execute permissions. The group had execute permission, which allowed members of the group to access the directory if they knew the names of its contents.

The organization required that only `researcher2`, the directory owner, be able to access the directory and its contents. I removed the group’s execute permission with the following command:

```bash
chmod g-x drafts
```

In this command:

* `g` represents the group.
* `-` removes a permission.
* `x` represents execute permission.
* `drafts` identifies the directory being modified.

I verified the change with:

```bash
ls -ld drafts
```

The updated permission string was:

```text
drwx------
```

The owner retained read, write, and execute permissions. The group and all other users had no permissions, ensuring that only `researcher2` could access the directory.

> Add a screenshot of the `chmod g-x drafts` command and verification output here if available.

## Security Principles Applied

The permission changes applied several foundational cybersecurity principles:

* **Least privilege:** Users received only the access required to perform their responsibilities.
* **Access control:** File and directory permissions were used to control who could read, modify, or access resources.
* **Authorization management:** Existing permissions were compared with organizational requirements and corrected when necessary.
* **Data protection:** Unauthorized write access was removed to reduce the risk of accidental or malicious changes.
* **Defense in depth:** Operating-system permissions provided an additional security layer for sensitive research information.

## Skills Developed

Through this project, the following skills were strengthened:

* Examining Linux file permissions
* Interpreting 10-character permission strings
* Differentiating user, group, and other permissions
* Using symbolic mode with `chmod`
* Working with hidden files
* Securing directories
* Applying the principle of least privilege
* Verifying permission changes
* Documenting Linux security procedures

## Conclusion

I used `ls -la` to examine all files and directories in the projects directory, including hidden files. I interpreted the permission strings and used `chmod` to remove unauthorized write access from `project_k.txt`, assign appropriate read-only permissions to `.project_x.txt`, and restrict the `drafts` directory so that only its owner could access it.

These changes ensured that the research team’s files and directories followed the organization’s authorization requirements. The project demonstrates how Linux permissions can be used to enforce least privilege and protect sensitive information from unauthorized access or modification.

