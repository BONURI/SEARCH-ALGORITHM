import pyglet
import random

# Create a window
window = pyglet.window.Window(width=1300, height=400, caption='Binary Search Visualization')
batch = pyglet.graphics.Batch()

# Generate a sorted list with random numbers ensuring 55 is included
numbers = sorted(random.sample(range(1, 100), 19) + [55])

# Variables to control the animation and search
left, right = 0, len(numbers) - 1
mid = (left + right) // 2
found = False
search_complete = False

def binary_search():
    global left, right, mid, found, search_complete
    if left <= right and not found:
        mid = (left + right) // 2
        if numbers[mid] == 55:
            found = True
        elif numbers[mid] < 55:
            left = mid + 1
        else:
            right = mid - 1
    else:
        search_complete = True

# Schedule the binary search to run every 3 seconds
pyglet.clock.schedule_interval(lambda dt: binary_search(), 3)

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        # Define the position and size of each 'box'
        x = i * 60 + 45
        y = window.height // 2
        radius = 25  # Define the radius for the circle

        # Draw the circle
        if left <= i <= right and not search_complete:
            color = (70, 130, 180) # steelBlue for the current search interval
        elif i == mid and not search_complete:
            color = (255, 127, 80)  # Coral for the middle element
        elif found and i == mid:
            color = (255, 105, 180)  # hotpink if 55 is found
        else:
            color = (176, 224, 230) # powderblueblue for eliminated elements
        
        pyglet.shapes.Circle(x + radius, y + radius, radius, color=color, batch=batch).draw()
        
        # Draw the number inside the circle
        label = pyglet.text.Label(str(number), x=x + radius, y=y + radius, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.app.run()
