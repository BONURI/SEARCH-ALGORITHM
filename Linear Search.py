import pyglet
import random

# Create a window
window = pyglet.window.Window(width=1300, height=400, caption='Linear Search Visualization')
batch = pyglet.graphics.Batch()

# Generate a list with random numbers ensuring 55 is included
numbers = random.sample(range(1, 100), 19) + [55]
random.shuffle(numbers)

# Variables to control the animation and search
current_index = 0
found_index = -1
search_complete = False

def linear_search():
    global current_index, found_index, search_complete
    if current_index < len(numbers):
        if numbers[current_index] == 55:
            found_index = current_index
            search_complete = True
        current_index += 1
    else:
        search_complete = True

# Schedule the linear search to run every 1 seconds
pyglet.clock.schedule_interval(lambda dt: linear_search(), 1)

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        # Define the position and size of each 'circle'
        x = i * 60 + 45
        y = window.height // 2
        radius = 25

        # Draw the circle
        if i == current_index and not search_complete:
            color = (176, 224, 230) #  for powderblue the current circle being checked
        elif i == found_index:
            color = (255, 105, 180)# hotpink if 55 is found
        else:
            color = (70, 130, 180)  # steelblue for unchecked or passed circles
        
        pyglet.shapes.Circle(x, y, radius, color=color, batch=batch).draw()
        # Draw the number inside the circle
        label = pyglet.text.Label(str(number), x=x, y=y, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.app.run()