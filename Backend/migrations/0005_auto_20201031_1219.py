# Generated by Django 3.1.2 on 2020-10-31 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0004_auto_20201031_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='act_animal',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='акт №'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='administrative_district_animal',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='административный округ'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='age_animal',
            field=models.CharField(default='', max_length=100, verbose_name='возраст'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='anamnesis_animal',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='анамнез'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='avairy_animal',
            field=models.CharField(default='', max_length=100, verbose_name='Вольер №'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='breed_animal',
            field=models.CharField(default='', max_length=100, verbose_name='порода'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='care_worker_animal',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='ф.и.о. сотрудника по уходу за животным'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='catch_report_animal',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='акт отлова №'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='color_animal',
            field=models.CharField(default='', max_length=100, verbose_name='окрас'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='contract_leaving_animal',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='акт/договор №'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='date_inspection_animal',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='дата осмотра'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='date_leaving_shelter_animal',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='дата выбытия из приюта'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='date_receipt_report_animal',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='заказ-наряд дата/ акт о поступлении животного, дата'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='date_treatment_parasite_animal',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='дата'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='date_vaccine_animal',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='дата'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='drug_dosage_animal',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='доза'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='drug_name_animal',
            field=models.CharField(default='', max_length=1000, null=True, verbose_name='название препарата'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ears_animal',
            field=models.CharField(default='', max_length=100, verbose_name='уши'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='exploit_organization_animal',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='эксплуатирующая организация'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='feature_animal',
            field=models.CharField(default='', max_length=100, verbose_name='особые приметы'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='gender_animal',
            field=models.CharField(default='', max_length=100, verbose_name='пол'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='hair_animal',
            field=models.CharField(default='', max_length=100, verbose_name='шерсть'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='head_ofshelter_animal',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='ф.и.о. руководителя приюта'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='idcard_registration_animal',
            field=models.CharField(default='', max_length=100, verbose_name='карточка учета животного №'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='identification_mark_animal',
            field=models.CharField(default='', max_length=100, verbose_name='идентификационная метка'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='item_no_treatment_animal',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='№ п/п(сведения об обработке от экто- и эндопаразитов)'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='legal_entity_animal',
            field=models.CharField(default='FFF', max_length=100, null=True, verbose_name='юридическое лицо'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='name_animal',
            field=models.CharField(default='', max_length=100, verbose_name='кличка'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='num_serial_animal',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='№ серии'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='receipt_report_animal',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='заказ-наряд / акт о поступлении животного №'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='size_animal',
            field=models.CharField(default='', max_length=100, verbose_name='размер'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='socialized_animal',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='Социализировано(да/нет)'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sterilization_date_animal',
            field=models.CharField(default='', max_length=100, verbose_name='дата стерилизации'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='tail_animal',
            field=models.CharField(default='', max_length=100, verbose_name='хвост'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='type_animal',
            field=models.CharField(default='', max_length=100, verbose_name='вид'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='type_vaccine_animal',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='вид вакцины'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='weight_animal',
            field=models.CharField(default='', max_length=100, verbose_name='вес'),
        ),
    ]