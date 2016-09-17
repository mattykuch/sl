# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vaccine_select', models.CharField(default=b'MEASLES', max_length=50, choices=[(b'MEASLES', b'Measles vaccine 10 dose Vial'), (b'BCG', b'Bacillus Calmette-Guerin 20 dose Vial'), (b'HPV', b'Human Papilloma Vaccine 1 dose Vial'), (b'HEPB', b'Hepatitis .B Vaccine 10 dose Vial'), (b'TT', b'Tetanus Toxoid Vaccine 20 dose Vial'), (b'OPV', b'Oral Polio Vaccine 20 dose Vial'), (b'YELLOWFEVER', b'Yellow Fever  10 dose Vial'), (b'PCV', b'Pneumococcal Conjugate 2 dose Vial'), (b'PENTA', b'DPT-HIP B-HEB 10 Dose Vial'), (b'IPV', b'Inactivated Polio vaccine 5 dose Vial'), (b'ROTA', b'Rotavirus vaccine 1 dose Vial'), (b'SYRINGE005', b'Syringe 0.05 ml'), (b'SYRINGE05', b'Syringe 0.5 ml'), (b'SYRINGE5', b'Syringe 5 ml'), (b'SYRINGE2', b'Syringe 2 ml'), (b'SB', b'Safety Boxes'), (b'TTCARDS', b'Tetanus Toxoid Cards'), (b'CHC', b'Child Health Cards'), (b'VCB', b'Vaccine Control Books')])),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
