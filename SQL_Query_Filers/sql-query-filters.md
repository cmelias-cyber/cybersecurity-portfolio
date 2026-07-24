# Apply Filters to SQL Queries

## Project Description (Executive Summary)

The purpose of this project was to use SQL to investigate potential security issues involving employee login activity and organizational devices. I queried the `log_in_attempts` and `employees` tables to retrieve records that matched specific security conditions.

Using `WHERE` clauses with the `AND`, `OR`, `NOT`, and `LIKE` operators, I identified failed after-hours logins, activity from specific dates and locations, and employee machines requiring security updates. These queries demonstrate how database filtering can support incident investigation, access monitoring, and security operations.

## Database Tables

The investigation used two tables from the organization’s database.

### `log_in_attempts`

This table contains information about employee login activity:

* `event_id` — Unique identification number for the login event
* `username` — Username associated with the attempt
* `login_date` — Date of the login attempt
* `login_time` — Time of the login attempt
* `country` — Country from which the attempt originated
* `ip_address` — IP address associated with the employee’s machine
* `success` — Whether the attempt succeeded; `FALSE` or `0` represents a failed attempt

### `employees`

This table contains information about employees and their assigned machines:

* `employee_id` — Unique identification number for the employee
* `device_id` — Identification number for the employee’s device
* `username` — Employee username
* `department` — Department in which the employee works
* `office` — Employee’s office location

## Retrieve After-Hours Failed Login Attempts

A potential security incident occurred after normal business hours. To investigate it, I retrieved all unsuccessful login attempts that occurred after 18:00.

```sql
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00:00'
  AND success = FALSE;
```

The `SELECT *` statement retrieves every column from the `log_in_attempts` table. The `WHERE` clause limits the output to records that meet two conditions.

The first condition, `login_time > '18:00:00'`, returns login attempts that occurred after 6:00 p.m. The second condition, `success = FALSE`, returns only failed attempts. The `AND` operator requires both conditions to be true for a record to appear in the results.

This query helps isolate failed authentication activity occurring outside normal business hours, which may require further investigation.

## Retrieve Login Attempts on Specific Dates

A suspicious event occurred on May 9, 2022. To examine activity related to the event, I retrieved login attempts from that date and the preceding day.

```sql
SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-09'
   OR login_date = '2022-05-08';
```

The query retrieves all columns from the `log_in_attempts` table. The first condition returns attempts recorded on May 9, 2022, while the second returns attempts recorded on May 8, 2022.

The `OR` operator allows a record to be returned when either condition is true. It is appropriate here because a single login attempt cannot have both dates simultaneously.

Filtering by specific dates helps establish a timeline of activity surrounding a suspected security event.

## Retrieve Login Attempts Outside Mexico

The security team determined that the suspicious activity did not originate in Mexico. I retrieved login attempts from every country other than Mexico.

```sql
SELECT *
FROM log_in_attempts
WHERE NOT country LIKE 'MEX%';
```

The `LIKE` operator searches for values that match a specified pattern. In this dataset, Mexico may appear as either `MEX` or `MEXICO`.

The pattern `'MEX%'` matches any value beginning with `MEX`. The percentage sign (`%`) is a wildcard representing zero or more unspecified characters. This allows the query to match both `MEX` and `MEXICO`.

The `NOT` operator excludes records that match this pattern. As a result, the query returns login attempts originating outside Mexico.

This query demonstrates how pattern matching and exclusion filters can support geographic analysis during a security investigation.

## Retrieve Employees in Marketing

The security team needed to update machines assigned to Marketing employees located in the East building.

```sql
SELECT *
FROM employees
WHERE department = 'Marketing'
  AND office LIKE 'East%';
```

The query retrieves records from the `employees` table that meet two conditions. The first condition, `department = 'Marketing'`, limits the results to employees in the Marketing department.

The second condition uses `office LIKE 'East%'` to return office values beginning with `East`, such as `East-170` or `East-320`. The `%` wildcard allows any office number to follow the building name.

The `AND` operator requires employees to satisfy both conditions. Therefore, the results include only Marketing employees whose offices are located in the East building.

This information can be used to identify the specific employee devices that require the security update.

## Retrieve Employees in Finance or Sales

A different security update was required for machines assigned to employees in the Finance and Sales departments.

```sql
SELECT *
FROM employees
WHERE department = 'Finance'
   OR department = 'Sales';
```

The first condition returns employees in Finance, while the second returns employees in Sales. The `OR` operator includes a record when either condition is true.

Using `OR` is necessary because an employee only needs to belong to one of the two departments to be included. Using `AND` would incorrectly require the same employee record to list both departments.

The results identify the employee accounts and associated devices requiring this specific update.

## Retrieve All Employees Not in Information Technology

Employees in the Information Technology department had already received the final security update. I retrieved employees from all other departments.

```sql
SELECT *
FROM employees
WHERE NOT department = 'Information Technology';
```

The query retrieves all employee records for which the department is not Information Technology. The `NOT` operator reverses the condition and excludes records that match the specified department.

The output can be used to identify all remaining employee machines that still require the update.

This query demonstrates how exclusion filters can prevent already-completed devices from being included in an update process.

## SQL Operators and Filtering Techniques

### `WHERE`

The `WHERE` clause limits query results to records that meet specified conditions. Without it, a `SELECT *` query would return every record in the selected table.

### `AND`

The `AND` operator requires all connected conditions to be true. It was used to identify:

* Failed login attempts occurring after 18:00
* Marketing employees located in the East building

### `OR`

The `OR` operator requires at least one connected condition to be true. It was used to identify:

* Login attempts occurring on either May 8 or May 9, 2022
* Employees belonging to either Finance or Sales

### `NOT`

The `NOT` operator excludes records that match a condition. It was used to identify:

* Login attempts originating outside Mexico
* Employees outside the Information Technology department

### `LIKE` and `%`

The `LIKE` operator searches for text values that match a pattern. The `%` wildcard represents zero or more characters.

For example:

```sql
country LIKE 'MEX%'
```

matches both `MEX` and `MEXICO`.

Similarly:

```sql
office LIKE 'East%'
```

matches office locations such as `East-170`, `East-320`, and any other value beginning with `East`.

## Security Principles Applied

The queries in this project support several cybersecurity practices:

* **Security monitoring:** Reviewing login records can help identify suspicious authentication behavior.
* **Incident investigation:** Date, time, and geographic filters help narrow large datasets to relevant events.
* **Access analysis:** Failed login attempts can indicate user error, credential misuse, or attempted unauthorized access.
* **Asset management:** Employee and device records help security teams determine which systems require updates.
* **Targeted remediation:** SQL filters allow updates and investigations to focus on affected users and machines.
* **Data-driven decision-making:** Query results provide evidence that can guide additional security actions.

## Skills Developed

Through this project, the following skills were strengthened:

* Writing structured SQL queries
* Retrieving data from relational database tables
* Filtering date and time values
* Combining multiple conditions
* Differentiating between `AND` and `OR`
* Excluding records with `NOT`
* Performing pattern searches with `LIKE`
* Using SQL wildcards
* Investigating authentication activity
* Identifying devices for targeted security updates
* Documenting technical findings

## Conclusion

I used SQL filters to investigate login activity and retrieve employee device information from the `log_in_attempts` and `employees` tables. I filtered failed after-hours logins, examined activity from specific dates, excluded login attempts originating in Mexico, and identified employees requiring different security updates.

The queries used `AND`, `OR`, `NOT`, `LIKE`, and the `%` wildcard to retrieve precise information from larger datasets. This project demonstrates how SQL can support security investigations, system monitoring, and targeted remediation activities.

