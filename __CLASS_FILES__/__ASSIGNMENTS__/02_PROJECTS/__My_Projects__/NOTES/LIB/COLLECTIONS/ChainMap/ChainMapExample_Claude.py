from collections import ChainMap

system_defaults = {
    'max_students': 30,
    'class_duration': 50,
    'attendance_required': True,
    'grading_scale': 'letter',
    'office_hours': 'By appointment',
    'textbook_required': True,
    'lab_access': False,
    'recording_enabled': False,
    'late_policy': 'No late submissions accepted',
    'participation_weight': 10,
    'homework_weight': 20,
    'exam_weight': 70,
    'building': 'Main Campus',
    'semester_length': 16,
    'credits': 3
}

# LAYER 2: Department-level configurations (overrides system defaults)
cs_department = {
    'max_students': 25,
    'lab_access': True,
    'recording_enabled': True,
    'textbook_required': False,
    'office_hours': 'Mon/Wed 2-4pm',
    'homework_weight': 30,
    'exam_weight': 60,
    'department': 'Computer Science',
    'building': 'Technology Center',
    'software_requirements': ['Python 3.11+', 'VS Code', 'Git'],
    'lab_fee': 50
}

cosc_1336_config = {
    'course_code': 'COSC-1336-009',
    'course_name': 'Programming Fundamentals I',
    'instructor': 'Professor Garcia',
    'max_students': 28,
    'class_duration': 75,
    'participation_weight': 15,
    'homework_weight': 25,
    'project_weight': 20,
    'exam_weight': 40,
    'late_policy': '10% penalty per day, max 3 days',
    'topics': ['Variables', 'Control Flow', 'Functions', 'OOP Basics'],
    'programming_language': 'Python',
    'ide_recommended': 'VS Code with Python extension'
}

section_009_overrides = {
    'section': '009',
    'meeting_times': 'MW 6:00-7:15 PM',
    'room': 'TC-204',
    'enrollment_current': 24,
    'teaching_assistant': 'Maria Rodriguez',
    'office_hours': 'Mon 5-6pm, Wed 7:15-8pm',
    'recording_enabled': True,
    'hybrid_option': True,
    'zoom_link': 'https://zoom.us/j/example',
    'discord_server': 'COSC1336-009-F2025'
}

student_accommodations = {
    'extended_time': True,
    'time_multiplier': 1.5,
    'separate_room': True,
    'note_taker': True,
    'recording_access': True,
    'late_policy': '20% penalty per day, max 5 days'
}

emergency_modifications = {
    'attendance_required': False,
    'meeting_times': 'Online Asynchronous',
    'recording_enabled': True,
    'late_policy': 'Extended deadlines - check announcements',
    'office_hours': 'Online via Zoom - check Discord'
}

finals_week_config = {
    'class_duration': 120,
    'meeting_times': 'Mon Dec 15, 6:00-8:00 PM',
    'room': 'TC-101',
    'attendance_required': True,
    'late_policy': 'No makeups without documented emergency'
}

summer_session_mods = {
    'semester_length': 8,
    'class_duration': 120,
    'meeting_times': 'MTWRF 9:00-11:00 AM',
    'max_students': 20,
    'homework_weight': 35,
    'exam_weight': 50,
    'late_policy': '20% penalty per day, max 2 days'
}

online_format = {
    'room': 'Online',
    'building': 'Virtual Campus',
    'recording_enabled': True,
    'attendance_required': False,
    'participation_weight': 5,
    'discussion_board_weight': 10,
    'lab_access': False,
    'lab_fee': 0,
    'software_requirements': ['Python 3.11+', 'VS Code', 'Git', 'Zoom', 'Discord']
}

standard_config = ChainMap(
    section_009_overrides,
    cosc_1336_config,
    cs_department,
    system_defaults
)

accommodated_config = ChainMap(
    student_accommodations,
    section_009_overrides,
    cosc_1336_config,
    cs_department,
    system_defaults
)

emergency_config = ChainMap(
    emergency_modifications,
    section_009_overrides,
    cosc_1336_config,
    cs_department,
    system_defaults
)

finals_config = ChainMap(
    finals_week_config,
    section_009_overrides,
    cosc_1336_config,
    cs_department,
    system_defaults
)

summer_config = ChainMap(
    summer_session_mods,
    cosc_1336_config,
    cs_department,
    system_defaults
)

online_config = ChainMap(
    online_format,
    cosc_1336_config,
    cs_department,
    system_defaults
)



