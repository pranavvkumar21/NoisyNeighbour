#!/usr/bin/env python3
from nicegui import ui

class Sidebar:
    def __init__(self):
        with ui.left_drawer():
            ui.label('Noisy Neighbour')
            ui.link('Home', '/')
            ui.link('Search', '/search')
            ui.link('Recordings', '/recordings')
            ui.link('Leaderboard', '/leaderboard')
            ui.link('Profile', '/profile')
            ui.link('Settings', '/settings')

class Topbar:
    def __init__(self):
        with ui.row().classes('w-full items-center p-2'):
            ui.input(placeholder='Search songs...').classes('w-full')

class MainArea:
    def __init__(self):
        with ui.column().classes('w-full items-center p-4'):
            ui.card().classes('w-full max-w-xl') \
                .content(ui.label('🎤 Featured Instrumental'))
            ui.audio(src='').classes('w-full max-w-xl')
            ui.textarea(placeholder='Lyrics...').classes('w-full max-w-xl')
            with ui.row().classes('w-full max-w-xl justify-around'):
                ui.button('Record')
                ui.button('Play')
                ui.button('Stop')

def create_app():
    Sidebar()
    Topbar()
    MainArea()
    ui.run(title='Noisy Neighbour', dark=True)

if __name__ == '__main__':
    create_app()
