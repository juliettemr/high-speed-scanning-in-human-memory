import random
from expyriment import design, control, stimuli

experiment = design.Experiment(name="High speed scanning")
control.initialize(experiment)

training_length = 24
test_length = 144
training_results = []
test_results = []

training_length2 = 60
test_length2 = 120
training_results2_1 = []
test_results2_1 = []
training_results2_2 = []
test_results2_2 = []
training_results2_3 = []
test_results2_3 = []

non_selected2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
set1 = []
set2 = []
set3 = []
set1.append(non_selected2.pop(random.randint(0, len(non_selected2) - 1)))
set2.append(non_selected2.pop(random.randint(0, len(non_selected2) - 1)))
set2.append(non_selected2.pop(random.randint(0, len(non_selected2) - 1)))
set3.append(non_selected2.pop(random.randint(0, len(non_selected2) - 1)))
set3.append(non_selected2.pop(random.randint(0, len(non_selected2) - 1)))
set3.append(non_selected2.pop(random.randint(0, len(non_selected2) - 1)))
set3.append(non_selected2.pop(random.randint(0, len(non_selected2) - 1)))

beep_sound = stimuli.Tone(duration = 200, frequency = 2000)
beep_sound.preload()

def series_experiment1(number, training = False):
    s = random.randint(1, 6)
    non_selected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    selected = []
    for i in range(s):
        selected.append(non_selected.pop(random.randint(0, len(non_selected) - 1)))

    if training:
        stimuli.TextLine("Training series {}".format(number)).present()
    else:
        stimuli.TextLine("Series {}".format(number)).present()
    experiment.clock.wait(1000)

    for digit in selected:
        stimuli.TextLine(str(digit)).present()
        experiment.clock.wait(1200)
    
    stimuli.BlankScreen().present()
    experiment.clock.wait(2000)
    
    beep_sound.present()
    is_test_selected = bool(random.randint(0, 1))
    stimuli.TextLine(str(random.choice(selected) if is_test_selected else random.choice(non_selected))).present()
    key, reaction_time = experiment.keyboard.wait([102, 106])
    result = ((key == 102) == is_test_selected, reaction_time)
    if result[0]:
        stimuli.TextLine("Your answer is correct! Your reaction time was {}ms".format(result[1]), text_colour=(0, 255, 0)).present()
    else:
        stimuli.TextLine("Your answer is wrong! Your reaction time was {}ms".format(result[1]), text_colour=(255, 0, 0)).present()
    experiment.clock.wait(1000)
    
    return result

def series_experiment2(number, step, training = False):
    if training:
        stimuli.TextLine("Training series {}".format(number)).present()
    else:
        stimuli.TextLine("Series {}".format(number)).present()
    experiment.clock.wait(1000)
    
    beep_sound.present()
    is_test_selected = random.randint(0, 14) <= 3
    if step == 1:
        selected = set1
    elif step == 2:
        selected = set2
    else:
        selected = set3
    stimuli.TextLine(str(random.choice(selected) if is_test_selected else random.choice(non_selected2))).present()
    key, reaction_time = experiment.keyboard.wait([102, 106])
    result = ((key == 102) == is_test_selected, reaction_time)
    if result[0]:
        stimuli.TextLine("Your answer is correct! Your reaction time was {}ms".format(result[1]), text_colour=(0, 255, 0)).present()
    else:
        stimuli.TextLine("Your answer is wrong! Your reaction time was {}ms".format(result[1]), text_colour=(255, 0, 0)).present()
    experiment.clock.wait(3700)
    
    return result

control.start()

stimuli.TextLine("During this first experiment, you will have to remember series of one to six digit(s). Then after the beep, you will have to determine if the digit displayed on the screen was in the series (press f) or not (press j).").present()
experiment.keyboard.wait()

stimuli.TextLine("Here is a warm-up, ready?").present()
experiment.keyboard.wait()

for i in range(training_length):
    training_results.append(series_experiment1(i + 1, training = True))

stimuli.TextLine("Now comes the real test, ready?").present()
experiment.keyboard.wait()

for i in range(test_length):
    test_results.append(series_experiment1(i + 1))

stimuli.TextLine("Good job! You finished the first experiment!").present()
experiment.keyboard.wait()

training_correctness = 0
training_timing = 0
test_correctness = 0
test_timing = 0
for result in training_results:
    if result[0]:
        training_correctness += 1
    training_timing += result[1]
for result in test_results:
    if result[0]:
        test_correctness += 1
    test_timing += result[1]
training_correctness = int(100 * training_correctness / training_length)
training_timing //= training_length
test_correctness = int(100 * test_correctness / test_length)
test_timing //= test_length

stimuli.TextLine("During the training, your accuracy was {}% and you took on average {}ms to respond.".format(training_correctness, training_timing)).present()
experiment.keyboard.wait()
stimuli.TextLine("During the test, your accuracy was {}% and you took on average {}ms to respond.".format(test_correctness, test_timing)).present()
experiment.keyboard.wait()

stimuli.TextLine("During this second experiment, you will have to remember you will have to remember a set of digits and determine if the digit displayed on the screen was in the set or (press f) or not (press j).").present()
experiment.keyboard.wait()

stimuli.TextLine("Here is a warm-up, ready?").present()
experiment.keyboard.wait()

stimuli.TextLine("Part 1: the set is {}".format(set1[0])).present()
experiment.keyboard.wait()

for i in range(training_length2):
    training_results2_1.append(series_experiment2(i + 1, 1, training = True))

stimuli.TextLine("Part 2: the set is {} {}".format(set2[0], set2[1])).present()
experiment.keyboard.wait()

for i in range(training_length2):
    training_results2_2.append(series_experiment2(i + 1, 2, training = True))

stimuli.TextLine("Part 3: the set is {} {} {} {}".format(set3[0], set3[1], set3[2], set3[3])).present()
experiment.keyboard.wait()

for i in range(training_length2):
    training_results2_3.append(series_experiment2(i + 1, 3, training = True))

stimuli.TextLine("Now comes the real test, ready?").present()
experiment.keyboard.wait()

stimuli.TextLine("Part 1: the set is {}".format(set1[0])).present()
experiment.keyboard.wait()

for i in range(training_length2):
    test_results2_1.append(series_experiment2(i + 1, 1))

stimuli.TextLine("Part 2: the set is {} {}".format(set2[0], set2[1])).present()
experiment.keyboard.wait()

for i in range(training_length2):
    test_results2_2.append(series_experiment2(i + 1, 2))

stimuli.TextLine("Part 3: the set is {} {} {} {}".format(set3[0], set3[1], set3[2], set3[3])).present()
experiment.keyboard.wait()

for i in range(training_length2):
    test_results2_3.append(series_experiment2(i + 1, 3))

stimuli.TextLine("Good job! You finished the second experiment!").present()
experiment.keyboard.wait()

training_correctness2_1 = 0
training_timing2_1 = 0
test_correctness2_1 = 0
test_timing2_1 = 0
for result in training_results2_1:
    if result[0]:
        training_correctness2_1 += 1
    training_timing2_1 += result[1]
for result in test_results2_1:
    if result[0]:
        test_correctness2_1 += 1
    test_timing2_1 += result[1]
training_correctness2_1 = int(100 * training_correctness2_1 / training_length2)
training_timing2_1 //= training_length2
test_correctness2_1 = int(100 * test_correctness2_1 / test_length2)
test_timing2_1 //= test_length2

stimuli.TextLine("During the training of part 1, your accuracy was {}% and you took on average {}ms to respond.".format(training_correctness2_1, training_timing2_1)).present()
experiment.keyboard.wait()
stimuli.TextLine("During the test of part 1, your accuracy was {}% and you took on average {}ms to respond.".format(test_correctness2_1, test_timing2_1)).present()
experiment.keyboard.wait()

training_correctness2_2 = 0
training_timing2_2 = 0
test_correctness2_2 = 0
test_timing2_2 = 0
for result in training_results2_2:
    if result[0]:
        training_correctness2_2 += 1
    training_timing2_2 += result[1]
for result in test_results2_2:
    if result[0]:
        test_correctness2_2 += 1
    test_timing2_2 += result[1]
training_correctness2_2 = int(100 * training_correctness2_2 / training_length2)
training_timing2_2 //= training_length2
test_correctness2_2 = int(100 * test_correctness2_2 / test_length2)
test_timing2_2 //= test_length2

stimuli.TextLine("During the training of part 2, your accuracy was {}% and you took on average {}ms to respond.".format(training_correctness2_2, training_timing2_2)).present()
experiment.keyboard.wait()
stimuli.TextLine("During the test of part 2, your accuracy was {}% and you took on average {}ms to respond.".format(test_correctness2_2, test_timing2_2)).present()
experiment.keyboard.wait()

training_correctness2_3 = 0
training_timing2_3 = 0
test_correctness2_3 = 0
test_timing2_3 = 0
for result in training_results2_3:
    if result[0]:
        training_correctness2_3 += 1
    training_timing2_3 += result[1]
for result in test_results2_3:
    if result[0]:
        test_correctness2_3 += 1
    test_timing2_3 += result[1]
training_correctness2_3 = int(100 * training_correctness2_3 / training_length2)
training_timing2_3 //= training_length2
test_correctness2_3 = int(100 * test_correctness2_3 / test_length2)
test_timing2_3 //= test_length2

stimuli.TextLine("During the training of part 3, your accuracy was {}% and you took on average {}ms to respond.".format(training_correctness2_3, training_timing2_3)).present()
experiment.keyboard.wait()
stimuli.TextLine("During the test of part 3, your accuracy was {}% and you took on average {}ms to respond.".format(test_correctness2_3, test_timing2_3)).present()
experiment.keyboard.wait()

control.end()
