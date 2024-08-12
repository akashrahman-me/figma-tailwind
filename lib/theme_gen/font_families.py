def font_families(fonts):
    font_groups = {}
    for font in fonts:
        font_family = font.get('fontFamily')
        font_weight = font.get('fontWeight')

        if font_family not in font_groups:
            font_groups[font_family] = {'name': font_family, 'weight': []}

        if font_weight not in font_groups[font_family]['weight']:
            font_groups[font_family]['weight'].append(font_weight)
            font_groups[font_family]['weight'].sort(key=float)

    return list(font_groups.values())
