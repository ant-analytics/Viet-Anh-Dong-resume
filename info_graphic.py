import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')
import pandas as pd

def plot_header(ax):
    brief_info = f'Curriculum Vitae\n'
    contact_info = f'Your Name\n'
    ax.text(0.5, 0.8, 'VIET ANH DONG', fontsize=24, fontweight='bold', ha='center', color='#2E4053')
    ax.text(0.5, 0.6, contact_info, fontsize=12, ha='center', color='#1F618D')
    ax.text(0.5, 0.4, brief_info, fontsize=12, ha='center', color='#1F618D')
    ax.axis('off')

def plot_professional_development(ax):
    life = pd.DataFrame({
        'events': ['Start Higher Education', 'Bachelor of Forestry', 'Forestry Officer', 'Master of Forestry', 'Forestry Officer', 'PhD in Forestry', 'Senior Forestry Officer', 'Relocating to Queensland - Australia', 'Become a Specialist in Data Analytics'], 
        'index': [2001, 2005, 2010, 2012, 2014, 2018, 2023, 2025, 2027]
    }).set_index('index')

    ax.scatter(life.index, range(len(life)), s=100, color='black', alpha=0.9)
    ax.plot(life.index, range(len(life)), color='black', linestyle='-', linewidth=2)

    ax.set_yticks(range(len(life)))
    ax.set_yticklabels(life['events'], fontsize=12, fontweight='bold')
    ax.set_xticks(life.index)
    ax.set_xticklabels(life.index, rotation=45, fontsize=12, fontweight='bold')
    ax.set_xlabel('Year', fontsize=12, fontweight='bold')

    ax.fill_between(life.index, range(len(life)), where=(life.index >= 2001) & (life.index <= 2010), color='lightgray', alpha=0.7, label='Vietnam')
    ax.fill_between(life.index, range(len(life)), where=(life.index >= 2010) & (life.index <= 2012), color='gray', alpha=0.7, label='Australia')
    ax.fill_between(life.index, range(len(life)), where=(life.index >= 2012) & (life.index <= 2014), color='lightgray', alpha=0.7)
    ax.fill_between(life.index, range(len(life)), where=(life.index >= 2014) & (life.index <= 2018), color='dimgray', alpha=0.7, label='New Zealand')
    ax.fill_between(life.index, range(len(life)), where=(life.index >= 2018) & (life.index <= 2023), color='lightgray', alpha=0.7)
    ax.fill_between(life.index, range(len(life)), where=(life.index >= 2023) & (life.index <= 2025), color='gray', alpha=0.7)
    ax.fill_between(life.index, range(len(life)), where=(life.index >= 2025) & (life.index <= 2027), color='gray', alpha=0.7)

    bbox_props = dict(boxstyle="round4", edgecolor="black", facecolor="white", alpha=0.9)
    el = plt.matplotlib.patches.Ellipse((0, 0), width=0.5, height=0.3, angle=0)

    ax.annotate('Received sponsorship from\nAustralian Government', xy=(2010, 2), xytext=(0.2, 0.5),
                textcoords='axes fraction',
                arrowprops=dict(arrowstyle="fancy", fc="0.6", ec="none", patchB=el,
                                connectionstyle="angle3,angleA=0,angleB=-90"),
                fontsize=12, color='black', bbox=bbox_props, wrap=True)

    ax.annotate('Received sponsorship from\nNew Zealand Government', xy=(2014, 4), xytext=(0.3, 0.6),
                textcoords='axes fraction',
                arrowprops=dict(arrowstyle="fancy", fc="0.6", ec="none", patchB=el,
                                connectionstyle="angle3,angleA=0,angleB=-90"),
                fontsize=12, color='black', bbox=bbox_props, wrap=True)

    ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Locations', title_fontsize='12', fontsize='12')

def plot_skills(ax):
    skills = pd.DataFrame({
        'skills': ['Python', 'R', 'SQL', 'Machine Learning', 'Data Visualization', 'Big Data', 'Deep Learning', 'NLP'],
        'percentage': [90, 80, 70, 80, 85, 70, 60, 50]
    }).sort_values(by='percentage', ascending=False)
    ax.barh(skills['skills'], skills['percentage'], color='#3498DB', alpha=0.7)
    ax.set_xlabel('Proficiency (%)', fontsize=10, fontweight='bold')
    ax.set_title('Skills Proficiency', fontsize=12, fontweight='bold')
    ax.grid(True, linestyle='--', alpha=0.6)

def plot_soft_skills(ax):
    soft_skills = pd.DataFrame({
        'soft_skills': ['Communication', 'Teamwork', 'Problem Solving', 'Adaptability', 'Leadership', 'Creativity'],
        'level': [85, 90, 80, 75, 70, 65]
    }).sort_values(by='level', ascending=False)
    ax.barh(soft_skills['soft_skills'], soft_skills['level'], color='#5D6D7E', alpha=0.7)
    ax.set_xlabel('Proficiency (%)', fontsize=10, fontweight='bold')
    ax.set_title('Soft Skills Proficiency', fontsize=12, fontweight='bold')

def plot_extra_info(ax):
    extra_info = """
    - Fluent in English and Vietnamese
    - Experienced in Agile methodologies
    - Strong analytical and problem-solving skills
    - Excellent written and verbal communication skills
    - Ability to work independently and as part of a team
    """
    ax.text(0, 1, extra_info, fontsize=10, ha='left', va='top', wrap=True, color='#1F618D')
    ax.axis('off')

mosaic = """
AAA
BBB
CCC
DDD
EEE
"""
fig, axes = plt.subplot_mosaic(mosaic, figsize=(21, 29.7))  # A4 portrait size in cm

# Adjust layout to add margins
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0.5)

# Plot each section
plot_header(axes['A'])
plot_professional_development(axes['B'])
plot_skills(axes['C'])
plot_soft_skills(axes['D'])
plot_extra_info(axes['E'])

plt.tight_layout()
plt.show()

# fig.savefig('cv_info_graphic.png', dpi=300, bbox_inches='tight')
fig, ax = plt.subplots(figsize=(10, 6))
a = plot_professional_development(ax)
fig.savefig('professional.png', dpi=300, bbox_inches='tight')