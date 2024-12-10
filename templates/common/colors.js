function shiftYellowToBlue(color) {
    // Convert a CSS color string (e.g., rgb, hex) to an RGB array
    function parseColor(color) {
        let match;
        if ((match = /^#([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(color))) {
            return match.slice(1).map((hex) => parseInt(hex, 16));
        } else if ((match = /^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/i.exec(color))) {
            return [parseInt(match[1]), parseInt(match[2]), parseInt(match[3])];
        }
        return null;
    }

    // Convert an RGB array back to a hex color string
    function rgbToHex([r, g, b]) {
        return `#${[r, g, b].map((val) => val.toString(16).padStart(2, '0')).join('')}`;
    }

    const rgb = parseColor(color);
    if (!rgb) return color; // Return unchanged if color can't be parsed

    // Identify yellowish colors (e.g., higher R and G values, lower B value)
    const [r, g, b] = rgb;
    if (r > 200 && g > 200 && b < 100) {
        // Shift toward bluish by reducing red and green, increasing blue
        return rgbToHex([Math.max(0, r - 100), Math.max(0, g - 100), Math.min(255, b + 100)]);
    }

    return color; // Return unchanged for non-yellowish colors
}

function updateCSSColors() {
    // Iterate through all stylesheets
    Array.from(document.styleSheets).forEach((sheet) => {
        try {
            Array.from(sheet.cssRules).forEach((rule) => {
                if (rule.style) {
                    Array.from(rule.style).forEach((property) => {
                        const value = rule.style.getPropertyValue(property).trim();
                        if (value.startsWith('#') || value.startsWith('rgb')) {
                            const newColor = shiftYellowToBlue(value);
                            if (newColor !== value) {
                                rule.style.setProperty(property, newColor);
                            }
                        }
                    });
                }
            });
        } catch (e) {
            console.warn('Could not access stylesheet:', sheet.href, e);
        }
    });

    // Update inline styles
    document.querySelectorAll('*').forEach((element) => {
        Array.from(element.style).forEach((property) => {
            const value = element.style.getPropertyValue(property).trim();
            if (value.startsWith('#') || value.startsWith('rgb')) {
                const newColor = shiftYellowToBlue(value);
                if (newColor !== value) {
                    element.style.setProperty(property, newColor);
                }
            }
        });
    });
}

// Execute the color shift
updateCSSColors();
