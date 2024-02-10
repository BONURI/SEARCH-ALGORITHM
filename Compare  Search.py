import pyglet
import random

# Create a window, adjust size if needed to better accommodate the layout
window = pyglet.window.Window(width=1500, height=800, caption='Search Algorithms Comparison')
batch = pyglet.graphics.Batch()

def reset_searches():
    global numbers, linear_index, linear_found, binary_left, binary_right, binary_mid, binary_found
    # Generate a list with random numbers and include 55, then sort it for binary search
    numbers = random.sample(range(1, 100), 31) + [55]
    random.shuffle(numbers)  # Shuffle for linear search
    numbers.sort()  # Sort for binary search

    # Reset search variables
    linear_index = 0
    linear_found = False
    binary_left, binary_right = 0, len(numbers) - 1
    binary_mid = (binary_left + binary_right) // 2
    binary_found = False

reset_searches()  # Initialize searches

def update_searches(dt):
    global linear_index, linear_found, binary_left, binary_right, binary_mid, binary_found

    # Update linear search
    if not linear_found and linear_index < len(numbers):
        if numbers[linear_index] == 55:
            linear_found = True
        linear_index += 1

    # Update binary search
    if not binary_found and binary_left <= binary_right:
        binary_mid = (binary_left + binary_right) // 2
        if numbers[binary_mid] == 55:
            binary_found = True
        elif numbers[binary_mid] < 55:
            binary_left = binary_mid + 1
        else:
            binary_right = binary_mid - 1

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.R:
        reset_searches()

pyglet.clock.schedule_interval(update_searches, 1)

@window.event
def on_draw():
    window.clear()
    margin = 5  # Margin between circles
    circle_radius = 20  # Radius of circles
    for i, number in enumerate(numbers):
        x = i * (circle_radius * 2 + margin) + circle_radius + margin  # Calculate x position with margin

        # Linear search circles (top half)
        y_linear = window.height * 3/4
        color_linear = (255, 105, 180) if linear_found and i == linear_index - 1 else (176, 224, 230) if i == linear_index else (70, 130, 180)
        pyglet.shapes.Circle(x, y_linear, circle_radius, color=color_linear, batch=batch).draw()

        # Binary search circles (bottom half)
        y_binary = window.height / 4
        color_binary = (255, 105, 180)if binary_found and i == binary_mid else(176, 224, 230) if binary_left <= i <= binary_right else  (70, 130, 180)
        pyglet.shapes.Circle(x, y_binary, circle_radius, color=color_binary, batch=batch).draw()

        # Draw the number inside each circle for both searches
        label = pyglet.text.Label(str(number), x=x, y=y_linear, anchor_x='center', anchor_y='center', color=(255, 255, 255,255), batch=batch)
        label.draw()
        label = pyglet.text.Label(str(number), x=x, y=y_binary, anchor_x='center', anchor_y='center', color=(255, 255, 255,255), batch=batch)
        label.draw()

pyglet.app.run()
