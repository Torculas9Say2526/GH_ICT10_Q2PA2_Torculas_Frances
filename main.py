# PA 2 
from pyscript import display, document

def club_member(e):
    document.getElementById('results').innerHTML = ' '
    last_name = document.getElementById('surname').value
    first_name = document.getElementById('first').value
    full_name = first_name + '' + last_name

    # these are the sets
    seven_sapphire = {'Miles Morales','Gwen Stacy','Aubrey Jules','Mila Watson'}
    eight_sapphire = {'Liam Johnnyson','Marie Wayne','Mika Yellow', 'Candice Noah'}
    nine_sapphire = {'Bennett John','Mike Wazowski','Boss Baby', 'Amber Stone'}
    ten_sapphire = {'Katharine Penas','Jaena Ambata', 'Adrianna Allas','Helena Magsino'}
    total_mems = seven_sapphire | eight_sapphire | nine_sapphire | ten_sapphire # Union
    total_mems.add(full_name)

    display(f'Here are all the members: {total_mems}', target='results')
    display(f'Total members: {len(total_mems)}', target='results')