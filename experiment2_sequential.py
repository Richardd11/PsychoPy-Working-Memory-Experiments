#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
EXPERIMENT 2: Sequential Memory Array Presentation - FULL ARRAY TEST
Working Memory with Cognitive Load and Mind Wandering

VERSION: 2.1.0 - REDESIGNED
4 colored squares shown ONE AT A TIME (sequential)
TEST: All 4 squares shown together again (one may change)

Based on: https://econtent.hogrefe.com/doi/10.1027/1618-3169/a000599
Modified: Full array comparison instead of single item
"""

from psychopy import visual, core, data, event, gui
from psychopy.hardware import keyboard
import random
import os
import csv
from datetime import datetime
from experiment_runtime import create_compatible_window, sanitize_participant_id

# ============================================
# TIMING CONSTANTS
# ============================================
FIXATION_DURATION = 0.5
MEMORY_DISPLAY_DURATION = 0.5
ISI_DURATION = 0.2
PARITY_TIMEOUT = 3.0
MEMORY_TEST_TIMEOUT = 5.0
LOAD_0_BLANK_DURATION = 6.0

# ============================================
# SETUP
# ============================================
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Participant info
expInfo = {
    'participant': '',
    'age': '',
    'gender': ['male', 'female', 'other', 'prefer not to say'],
    'session': '001'
}

dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title='Experiment 2 - Sequential (Full Array)')
if not dlg.OK:
    core.quit()

# Validate participant ID
if not expInfo['participant'].strip():
    error_dlg = gui.Dlg(title="Error")
    error_dlg.addText("Participant ID cannot be empty!")
    error_dlg.show()
    core.quit()

expInfo['participant'] = sanitize_participant_id(expInfo['participant'])

expInfo['date'] = data.getDateStr()
filename = _thisDir + os.sep + f'data/{expInfo["participant"]}_Experiment2_Sequential_FullArray_{expInfo["date"]}'
csv_filename = filename + '_data.csv'

# Check for duplicates
if os.path.exists(csv_filename):
    overwrite_dlg = gui.Dlg(title="File Exists")
    overwrite_dlg.addText(f"Data file already exists!")
    overwrite_dlg.addField('Action:', choices=['Cancel', 'Overwrite', 'New Session'])
    result = overwrite_dlg.show()
    if result is None or result[0] == 'Cancel':
        core.quit()
    elif result[0] == 'New Session':
        csv_filename = filename + f'_{datetime.now().strftime("%H%M%S")}_data.csv'

# Create and fully render-test the window. If a graphics error appears only
# during the first draw/flip, this also retries using safer windowed modes.
win, frameRate, frameDur = create_compatible_window(visual, core)

globalClock = core.Clock()

# ============================================
# STIMULI DEFINITION
# ============================================
COLORS = {
    'red': [1, -1, -1], 'green': [-1, 1, -1], 'blue': [-1, -1, 1],
    'yellow': [1, 1, -1], 'magenta': [1, -1, 1], 'cyan': [-1, 1, 1],
    'white': [1, 1, 1], 'orange': [1, 0.5, -1]
}
COLOR_NAMES = list(COLORS.keys())

POSITIONS = [[-0.2, 0.2], [0.2, 0.2], [-0.2, -0.2], [0.2, -0.2]]

THOUGHT_PROBE_CATEGORIES = {
    '1': 'Task', '2': 'Task experience/performance', '3': 'Everyday things',
    '4': 'Current state of being', '5': 'Personal worries', '6': 'Daydreams',
    '7': 'External environment', '8': 'Other'
}

# ============================================
# DATA FILE
# ============================================
print("Creating data file...")
try:
    # Create data folder if it doesn't exist
    import os
    if not os.path.exists('data'):
        os.makedirs('data')
        print("Created 'data' folder")
    
    csv_file = open(csv_filename, 'w', newline='', encoding='utf-8')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([
        'participant', 'session', 'date', 'age', 'gender',
        'trial_number', 'load_condition', 'change_condition', 'changed_position',
        'original_color_1', 'original_color_2', 'original_color_3', 'original_color_4',
        'test_color_1', 'test_color_2', 'test_color_3', 'test_color_4',
        'parity_digit_1', 'parity_response_1', 'parity_correct_1', 'parity_rt_1',
        'parity_digit_2', 'parity_response_2', 'parity_correct_2', 'parity_rt_2',
        'parity_digit_3', 'parity_response_3', 'parity_correct_3', 'parity_rt_3',
        'parity_digit_4', 'parity_response_4', 'parity_correct_4', 'parity_rt_4',
        'memory_response', 'memory_correct', 'memory_rt',
        'thought_probe_response', 'thought_probe_label', 'thought_probe_rt',
        'trial_start_time', 'trial_end_time', 'trial_duration'
    ])
    print(f"Data file created: {csv_filename}")
except Exception as e:
    print(f"ERROR creating data file: {e}")
    error_text = visual.TextStim(win, text=f"""ERROR: Cannot create data file!

Error: {str(e)}

Make sure you have write permissions in this folder.

Press SPACE to exit.""", height=0.04, wrapWidth=1.5, color='white')
    error_text.draw()
    win.flip()
    event.waitKeys(keyList=['space', 'escape'])
    win.close()
    core.quit()

# ============================================
# HELPER FUNCTIONS
# ============================================
def show_text(text, keys=None):
    text_stim = visual.TextStim(win, text=text, height=0.04, wrapWidth=1.5, color='white')
    text_stim.draw()
    win.flip()
    if keys:
        event.clearEvents()
        keys_pressed = event.waitKeys(keyList=keys + ['escape'])
        if 'escape' in keys_pressed:
            csv_file.close()
            win.close()
            core.quit()
        return keys_pressed

def show_fixation():
    fixation = visual.TextStim(win, text='+', height=0.1, color='white')
    frames = int(round(FIXATION_DURATION / frameDur))
    for _ in range(frames):
        fixation.draw()
        win.flip()

def show_memory_array_sequential(colors, positions):
    """Show 4 squares ONE AT A TIME (sequential)"""
    for i in range(4):
        square = visual.Rect(win, width=0.1, height=0.1, pos=positions[i],
                            fillColor=COLORS[colors[i]])
        frames = int(round(MEMORY_DISPLAY_DURATION / frameDur))
        for _ in range(frames):
            square.draw()
            win.flip()
        
        # ISI between squares
        if i < 3:
            show_blank(ISI_DURATION)

def show_blank(duration):
    frames = int(round(duration / frameDur))
    for _ in range(frames):
        win.flip()

def run_parity_task(load):
    if load == 0:
        show_blank(LOAD_0_BLANK_DURATION)
        return [{'digit': 'NA', 'response': 'NA', 'correct': 'NA', 'rt': 'NA'}] * 4
    
    digits = [random.choice([1,2,3,4,6,7,8,9]) for _ in range(load)]
    parity_data = []
    
    inst = visual.TextStim(win, text='F = ODD    J = EVEN', pos=[0, 0.35], height=0.03)
    digit_stim = visual.TextStim(win, text='', height=0.15)
    kb = keyboard.Keyboard()
    
    for digit in digits:
        kb.clearEvents()
        kb.clock.reset()
        digit_stim.text = str(digit)
        inst.draw()
        digit_stim.draw()
        win.flip()
        
        keys = kb.waitKeys(maxWait=PARITY_TIMEOUT, keyList=['f','j','escape'])
        if keys and 'escape' in keys:
            csv_file.close()
            win.close()
            core.quit()
        
        if keys:
            response = keys[0].name
            rt = keys[0].rt
            is_odd = digit % 2 == 1
            correct = 1 if (response == 'f' and is_odd) or (response == 'j' and not is_odd) else 0
            parity_data.append({'digit': digit, 'response': response, 'correct': correct, 'rt': rt})
        else:
            parity_data.append({'digit': digit, 'response': 'NA', 'correct': 0, 'rt': 'NA'})
        show_blank(ISI_DURATION)
    
    # Compensatory blank for load 2
    if load == 2:
        show_blank(3.0)
    
    while len(parity_data) < 4:
        parity_data.append({'digit': 'NA', 'response': 'NA', 'correct': 'NA', 'rt': 'NA'})
    return parity_data

def run_memory_test_full_array(original_colors, positions, change_cond):
    """
    NEW: Show ALL 4 squares TOGETHER and ask if they're all the same
    """
    # Create test colors
    test_colors = original_colors.copy()
    changed_pos = None
    
    if change_cond == 'change':
        # Pick random position to change
        changed_pos = random.randint(0, 3)
        # Get a different color
        available_colors = [c for c in COLOR_NAMES if c not in original_colors]
        test_colors[changed_pos] = random.choice(available_colors)
    
    # Show all 4 test squares TOGETHER
    squares = [visual.Rect(win, width=0.1, height=0.1, pos=positions[i],
                           fillColor=COLORS[test_colors[i]]) for i in range(4)]
    
    inst = visual.TextStim(win, text='Are all 4 colors the SAME as before?\n\nS = SAME (all identical)\nD = DIFFERENT (at least one changed)', 
                          pos=[0, 0.35], height=0.03)
    
    kb = keyboard.Keyboard()
    kb.clearEvents()
    kb.clock.reset()
    
    # Draw instruction and all squares
    inst.draw()
    for square in squares:
        square.draw()
    win.flip()
    
    keys = kb.waitKeys(maxWait=MEMORY_TEST_TIMEOUT, keyList=['s','d','escape'])
    if keys and 'escape' in keys:
        csv_file.close()
        win.close()
        core.quit()
    
    if keys:
        response = keys[0].name
        rt = keys[0].rt
        correct = 1 if (response == 's' and change_cond == 'no_change') or (response == 'd' and change_cond == 'change') else 0
        return {
            'test_colors': test_colors,
            'changed_position': changed_pos if changed_pos is not None else 'NA',
            'response': response, 
            'correct': correct, 
            'rt': rt
        }
    return {
        'test_colors': test_colors,
        'changed_position': changed_pos if changed_pos is not None else 'NA',
        'response': 'NA', 
        'correct': 0, 
        'rt': 'NA'
    }

def run_thought_probe():
    text = """What were you just thinking about?

1 = Task
2 = Task experience/performance
3 = Everyday things
4 = Current state of being
5 = Personal worries
6 = Daydreams
7 = External environment
8 = Other

Press the number."""
    
    text_stim = visual.TextStim(win, text=text, height=0.03, wrapWidth=1.5)
    text_stim.draw()
    win.flip()
    kb = keyboard.Keyboard()
    kb.clearEvents()
    kb.clock.reset()
    keys = kb.waitKeys(keyList=['1','2','3','4','5','6','7','8','escape'])
    
    if keys and 'escape' in keys:
        csv_file.close()
        win.close()
        core.quit()
    
    if keys:
        response = keys[0].name
        return {'response': response, 'label': THOUGHT_PROBE_CATEGORIES[response], 'rt': keys[0].rt}
    return {'response': 'NA', 'label': 'NA', 'rt': 'NA'}

def run_trial(trial_info):
    trial_start = globalClock.getTime()
    
    colors = random.sample(COLOR_NAMES, 4)
    
    show_fixation()
    show_memory_array_sequential(colors, POSITIONS)  # ONE AT A TIME
    show_blank(ISI_DURATION)
    
    parity_data = run_parity_task(int(trial_info['load_condition']))
    memory_data = run_memory_test_full_array(colors, POSITIONS, trial_info['change_condition'])
    thought_data = run_thought_probe()
    
    trial_end = globalClock.getTime()
    
    row = [
        expInfo['participant'], expInfo['session'], expInfo['date'], expInfo['age'], expInfo['gender'],
        trial_info['trial_number'], trial_info['load_condition'], trial_info['change_condition'], 
        memory_data['changed_position'],
        colors[0], colors[1], colors[2], colors[3],
        memory_data['test_colors'][0], memory_data['test_colors'][1], 
        memory_data['test_colors'][2], memory_data['test_colors'][3],
        parity_data[0]['digit'], parity_data[0]['response'], parity_data[0]['correct'], parity_data[0]['rt'],
        parity_data[1]['digit'], parity_data[1]['response'], parity_data[1]['correct'], parity_data[1]['rt'],
        parity_data[2]['digit'], parity_data[2]['response'], parity_data[2]['correct'], parity_data[2]['rt'],
        parity_data[3]['digit'], parity_data[3]['response'], parity_data[3]['correct'], parity_data[3]['rt'],
        memory_data['response'], memory_data['correct'], memory_data['rt'],
        thought_data['response'], thought_data['label'], thought_data['rt'],
        trial_start, trial_end, trial_end - trial_start
    ]
    csv_writer.writerow(row)
    csv_file.flush()

# ============================================
# MAIN EXPERIMENT
# ============================================
show_text("""EXPERIMENT 2: Sequential Presentation - FULL ARRAY TEST

You will see 4 colored squares appear ONE AT A TIME.

REMEMBER all 4 colors!

After a delay and some tasks, you will see 4 colored squares TOGETHER.

Your task: Decide if ALL 4 colors are the SAME as before,
or if at least ONE color changed.

S = SAME (all 4 identical)
D = DIFFERENT (at least 1 changed)

Press SPACE to start practice.""", keys=['space'])

# Practice
try:
    practice_trials = data.importConditions('conditions/practice_conditions.csv')
except Exception as e:
    error_msg = f"""ERROR: Cannot load practice conditions file!

Error: {str(e)}

Please make sure:
1. The 'conditions' folder exists
2. The file 'practice_conditions.csv' is in the conditions folder

Press SPACE to exit."""
    show_text(error_msg, keys=['space'])
    csv_file.close()
    win.close()
    core.quit()

for trial in practice_trials[:6]:
    run_trial(trial)

show_text("""Practice complete!

Remember:
- Memorize ALL 4 colors (shown one by one)
- After tasks, check if ALL are the same
- S = All SAME | D = At least one DIFFERENT

Press SPACE to begin the main experiment.

You will complete 144 trials with breaks every 36 trials.""", keys=['space'])

# Main experiment
try:
    main_trials = data.importConditions('conditions/experiment2_conditions.csv')
except Exception as e:
    error_msg = f"""ERROR: Cannot load main experiment conditions file!

Error: {str(e)}

Please make sure:
1. The 'conditions' folder exists
2. The file 'experiment2_conditions.csv' is in the conditions folder

Press SPACE to exit."""
    show_text(error_msg, keys=['space'])
    csv_file.close()
    win.close()
    core.quit()

random.shuffle(main_trials)

for i, trial in enumerate(main_trials):
    run_trial(trial)
    if (i + 1) % 36 == 0 and (i + 1) < len(main_trials):
        show_text(f"""Break time!

{i+1} of {len(main_trials)} trials complete.

Press SPACE to continue.""", keys=['space'])

show_text("""Experiment 2 Complete!

Thank you for your participation!

Data saved in: data/ folder

Press SPACE to exit.""", keys=['space'])

# Final pause before closing (prevents auto-close in Coder)
final_msg = visual.TextStim(win, text="""Thank you!

Closing in 3 seconds...

(Press ESC to close immediately)""", height=0.05, wrapWidth=1.5, color='white')
final_msg.draw()
win.flip()

# Wait 3 seconds or until ESC pressed
event.clearEvents()
core.wait(3.0, hogCPUperiod=0.2)

csv_file.close()
win.close()
core.quit()
