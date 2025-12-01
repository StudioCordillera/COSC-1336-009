"""_____________________________________________________________________________________________________________________________

Project 7 - Employee Management (OOP Design Note)
=================================================

Purpose
-------
This module implements an employee management system using OOP:

- Register new employees from user input.
- Manage a collection of employees (list, edit, archive, delete).
- Persist employees and company settings to a file (load/save).
- Support configurable company settings (name, email domain).
- Prepare for future extensions while staying simple and readable.

_____________________________________________________________________________________________________________________________

+-----------------------------------------------+
|                  Employee                     |
+-----------------------------------------------+
| - __first: str                                |  # always lower()
| - __last: str                                 |  # always lower()
| - __dependents: int                           |  # 0..10 inclusive
| - __wage: int                                 |  # stored as integer (e.g., 20)
| - __ssn: str                                  |  # "xxxxxxxxx" (9 digits, canonical)
| - __is_archived: bool                         |
+-----------------------------------------------+
| + get_first() -> str                          |
| + set_first(first: str)                       |
| + get_last() -> str                           |
| + set_last(last: str)                         |
| + get_dependents() -> int                     |
| + set_dependents(dependents: int)             | 
| + get_wage() -> int                           |
| + set_wage(wage: int)                         |
| + get_ssn() -> str                            |
| + set_ssn(ssn_raw: str)                       |  # normalizes to "xxxxxxxxx" or raises
| + is_archived() -> bool                       |
| + archive() -> None                           |
| + unarchive() -> None                         |
|                                               |
| # Computed / formatted values (no extra state)|
| + get_initials() -> str                       |  # (f"{first[0]}{last[0]}").upper()
| + get_email(domain: str) -> str               |  # f"{first}{last}@{domain}"
| + get_ssn_last4() -> str                      |  # ssn[-4:]
| + get_wage_formatted() -> str                 |  # f"${wage}"
| + get_ssn_formatted() -> str                  |  # "xxx-xx-xxxx"
| + get_employee_id() -> str                    |  # f"{last}.{ssn[-4:]}"
|                                               |
| + to_dict() -> dict                           |
| + @classmethod from_dict(d: dict) -> Employee |
+-----------------------------------------------+


    Employee Attributes & Rules
    ---------------------------

        Input-driven (stored)
        ~~~~~~~~~~~~~~~~~~~~~
        - first: str
          - stored as lowercase
          - validated: non-empty, alphabetical (simple check)

        - last: str
          - stored as lowercase
          - validated: non-empty, alphabetical

        - dependents: int
          - validated range: 0-10 inclusive

        - wage: int
          - stored as integer (e.g. 20)
          - formatted for display as: f"${wage}"

        - ssn: str (canonical internal storage)
          - internal canonical form: "xxxxxxxxx" (9 digits, no dashes)
          - accepted input forms:
            - "xxxxxxxxx" (all digits)
            - "xxx-xx-xxxx" (with dashes)
          - repository / helper normalizes to canonical string or raises if invalid
          - formatted for display as: "xxx-xx-xxxx"


        Derived / computed (not stored)
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        - initials: str
          - (f"{first[0]}{last[0]}").upper()  -> "FL"

        - email: str
          - domain is provided by repository (`repo.get_domain()`)
          - f"{first}{last}@{domain}"

        - ssn_last4: str
          - ssn[-4:]

        - employee_id (eID): str
          - f"{last}.{ssn_last4}"
          - used to identify/select employees in menus

_____________________________________________________________________________________________________________________________

+--------------------------------------------------+
|              EmployeeRepository                  |
+--------------------------------------------------+
| - filename: str                                  |
| - employees: list[Employee]                      |
| - company_name: str                              |
| - domain: str                                    |
+--------------------------------------------------+
| + __init__(filename: str,                       |
|            company_name: str, domain: str)       |
| + load() -> None                                 |
| + save() -> None                                 |
|                                                  |
| + add(emp: Employee) -> None                     |
| + list_all() -> list[Employee]                   |  # includes archived
| + list_active() -> list[Employee]                |  # excludes archived
| + find_by_eid(eid: str) -> Employee | None       |
| + remove_by_eid(eid: str) -> bool                |  # hard delete
|                                                  |
| + get_company_name() -> str                      |
| + set_company_name(name: str) -> None            |
| + get_domain() -> str                            |
| + set_domain(domain: str) -> None                |
|                                                  |
| + validate_domain(domain: str) -> (bool, str)    |
|   # returns (is_valid_format, warning_message)   |
|                                                  |
| + normalize_ssn(raw: str) -> str                 |
|   # accepts 'xxxxxxxxx' or 'xxx-xx-xxxx',        |
|   # returns canonical 'xxxxxxxxx' or raises      |
+--------------------------------------------------+


Company Settings
----------------
Stored in EmployeeRepository:

    - company_name: str
    - domain: str
      - user-settable via settings menu
      - basic validation in `validate_domain`:
        - Check simple pattern: something like "name.tld"
        - Recognize a simple list of common TLDs (".com", ".net", ".org", etc.)
        - If format or extension is questionable, still allow but return warning so UI can show:
          - "Warning: Domain extension not recognized."
          - "Warning: Format does not match standard (domain.com) format."

_____________________________________________________________________________________________________________________________

+----------------------------------------+
|                 App                    |
+----------------------------------------+
| - repo: EmployeeRepository             |
| - running: bool                        |
+----------------------------------------+
| + run() -> None                        |  # main loop
|                                        |
| - main_menu() -> None                  |  # r / m / c / e
|                                        |
| # Employee registration flow ("r")     |
| - flow_register_employee() -> None     |
|   - step_reg_input() -> Employee       |
|   - step_reg_review(emp: Employee)     |
|   - step_reg_finalize(emp: Employee)   |
|                                        |
| # Employee collection management ("m") |
| - flow_manage_collection() -> None     |
|   - step_list_employees() -> None      |
|   - step_select_employee() -> Employee |
|   - step_manage_employee(emp) -> None  |
|     - step_edit_employee(emp) -> None  |
|     - step_archive_employee(emp) -> None|
|     - step_delete_employee(emp) -> None|
|                                        |
| # Company settings ("c")               |
| - flow_company_settings() -> None      |
|   - step_change_company_name() -> None |
|   - step_change_domain() -> None       |
+----------------------------------------+


Menu Flow Mapping to Methods
----------------------------

    Main Menu (App.main_menu)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
        Options:
        - r. Register New Employee
          -> App.flow_register_employee()
        - m. Manage Employees Collection
          -> App.flow_manage_collection()
        - c. Change Company Settings
          -> App.flow_company_settings()
        - e. Exit
          -> stop main loop and trigger repo.save()

    Register New Employee (r)
    ~~~~~~~~~~~~~~~~~~~~~~~~~
        1. Get input
           - App.step_reg_input()
           - Collect: first, last, dependents, ssn, wage
           - Use repository helpers (normalize_ssn, etc.) for validation

        1.1 Check input / review
           - App.step_reg_review(emp)
           - Display all fields:
             - 1. First Name
             - 2. Last Name
             - 3. Dependents
             - 4. SSN (formatted)
             - 5. Wage (formatted)
           - Options:
             - #. Change selected item
             - a. Change all items (re-run step_reg_input)
             - f. Finalize Employee Intake (go to 1.2)
             - c. Cancel New Employee Registration

        1.2 Finalize Employee In-Take
           - App.step_reg_finalize(emp)
           - Display summary:
             - Initials
             - Last, First
             - SSN (formatted)
             - Dependents
             - Wage (formatted)
             - Email
             - eID
           - Options:
             - #. Manually edit fields (limited edits)
             - f. Finalize Employee (repo.add(emp))
             - c. Cancel Registration


    Manage Employee Collection (m)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        2. Show list of Employees
           - App.step_list_employees()
           - Use repo.list_active() or repo.list_all()
           - Header: "Company Name | domain.com"
           - Rows: "eID | Employee" (e.g. "doe.1234 | Doe, John")

        Select Employee
           - App.step_select_employee()
           - "Provide an eID to manage an employee (or c to cancel)"

        2.1 Manage employee
           - App.step_manage_employee(emp)
           - Menu:
             - e. Edit Employee Info  -> step_edit_employee(emp)
             - a. Archive Employee     -> step_archive_employee(emp)
             - d. Delete Employee      -> step_delete_employee(emp)
             - c. Cancel

        2.2 Edit employee info (e)
           - App.step_edit_employee(emp)
           - Menu shows:
             1. Initials       (computed)
             2. Last           (stored)
             3. First          (stored)
             4. SSN            (stored, formatted)
             5. Dependents     (stored)
             6. Wage           (stored)
             7. Email          (computed)
             8. eID            (computed)
           - Options:
             - #. Manually edit fields (apply validation)
             - a. Finalize Employee (save changes and return)
             - c. Cancel Employee Edit (discard or confirm behavior)

        2.2 Archive employee (a)
           - App.step_archive_employee(emp)
           - Confirmation:
             - "Are you sure you want to ARCHIVE eID: lName, fName?"
             - y. Yes, archive employee (emp.archive())
             - c. Cancel

        2.3 Delete employee (d)
           - App.step_delete_employee(emp)
           - Confirmation:
             - "Are you sure you want to DELETE eID: lName, fName?"
             - y. Yes, delete employee (repo.remove_by_eid(eid))
             - c. Cancel


    Change Company Settings (c)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        - App.flow_company_settings()

        1. Company Name
        2. Domain

            Options:
            - #. edit item
            - c. Cancel

            3.1 Change Company Name
            - App.step_change_company_name()
            - Input: new company name
            - Show:
              - "Company Name will be changed from (old name) to (new name)."
            - Options:
              - a. Apply changes (repo.set_company_name(new_name))
              - e. Edit New Company Name
              - c. Cancel

            3.2 Change Company Domain
            - App.step_change_domain()
            - Input: new domain (e.g. "domain.com")
            - Call repo.validate_domain(new_domain)

            Case 1: domain extension not recognized or format issues
            - Show warnings:
              - "Warning: Domain extension not recognized."
              - and/or
              - "Warning: Format does not match standard (domain.com) format."
            - Show:
              - "Company Domain will be changed from (old domain) to (new domain)."
            - Options:
              - a. Apply Changes (still allowed)
              - e. Edit New Domain
              - c. Cancel

            Case 2: domain extension recognized and format OK
            - Show:
              - "Company Domain will be changed from (old domain) to (new domain)."
            - Options:
              - a. Apply Changes (repo.set_domain(new_domain))
              - e. Edit New Domain
              - c. Cancel

______________________________________________________________________________________________________________________________

Persistence Strategy
--------------------
- All persistent data (employees, company_name, domain) stored via EmployeeRepository.
- Suggested format: JSON file `filename` with structure:
  {
    "company_name": "...",
    "domain": "domain.com",
    "employees": [
      { ... employee dict from Employee.to_dict() ... },
      ...
    ]
  }
- On start:
  - repo.load() reads file (if present), reconstructs Employee objects with Employee.from_dict().
- On exit or key checkpoints:
  - repo.save() writes current state to disk.

_____________________________________________________________________________________________________________________________
  
Design Principles Applied
-------------------------
- Single Responsibility:
  - Employee: represents one employee and its logic.
  - EmployeeRepository: manages storage, collection operations, and configuration.
  - App: owns all user interaction and menu flow.
- Canonical Internal State:
  - Normalize SSN and name casing on input.
  - Derived values (email, eID, formatted strings) computed on request.
- Extensibility:
  - `is_archived` flag supports future reporting without data loss.
  - Repository can be swapped to a different storage backend in the future with minimal changes to App/Employee.

_____________________________________________________________________________________________________________________________"""