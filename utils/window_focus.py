import pygetwindow as gw
import logging

def focus_browser():
    try:
        browser_names = ['chrome', 'firefox', 'edge', 'opera', 'safari']
        for title in gw.getAllTitles():
            if any(browser in title.lower() for browser in browser_names):
                window = gw.getWindowsWithTitle(title)[0]
                window.activate()
                logging.info(f"Focused browser: {title}")
                return True
        logging.warning("No browser window found.")
        return False
    except Exception as e:
        logging.error(f"Error focusing browser: {e}")
        return False
