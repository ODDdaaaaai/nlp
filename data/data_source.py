# coding=utf-8
from model.Event import Event

# Events to search for
HAPPY_EVENTS = [
    Event(['فطر', 'عيد', 'سعيد', 'كل عام و أنتم بخير'], '2016-7-5', '2016-7-8', ['مصر', 'السعودية']),
    Event(['الفطر', 'عيد', 'سعيد', 'كل عام و أنتم بخير'], '2017-6-24', '2017-6-27', ['مصر', 'السعودية']),
    Event(['فطر', 'عيد', 'سعيد', 'كل عام و أنتم بخير'], '2018-6-14', '2018-6-16', ['مصر', 'السعودية']),

    Event(['الأضحى', 'عيد', 'سعيد', 'كل عام و أنتم بخير'], '2016-9-11', '2016-9-15', ['مصر', 'السعودية']),
    Event(['الأضحى', 'عيد', 'سعيد', 'كل عام و أنتم بخير'], '2017-8-31', '2018-9-4', ['مصر', 'السعودية']),
    Event(['الأضحى', 'عيد', 'سعيد', 'كل عام و أنتم بخير'], '2018-8-20', '2018-8-24', ['مصر', 'السعودية']),

    Event(['المولد', 'كل عام وانتم بخير'], '2016-12-10', '2016-12-10', ['مصر', 'السعودية']),
    Event(['المولد', 'كل عام وانتم بخير'], '2017-11-30', '2017-12-1', ['مصر', 'السعودية']),
    Event(['المولد', 'كل عام وانتم بخير'], '2018-11-19', '2018-11-21', ['مصر', 'السعودية']),

    Event(['السنة الهجرية', 'كل عام وانتم بخير'], '2016-10-1', '2016-10-1', ['مصر', 'السعودية']),
    Event(['السنة الهجرية', 'كل عام وانتم بخير'], '2017-9-20', '2017-9-21', ['مصر', 'السعودية']),
    Event(['السنة الهجرية', 'كل عام وانتم بخير'], '2018-9-10', '2018-9-11', ['مصر', 'السعودية']),

    Event(['المسيح', 'كريسمس', 'عيد مجيد', 'ميلاد', "سعيد"], '2016-12-24', '2016-12-25', ['مصر', 'السعودية']),
    Event(['المسيح', 'كريسمس', 'عيد مجيد', 'ميلاد', "سعيد"], '2017-12-24', '2017-12-25', ['مصر', 'السعودية']),
    Event(['المسيح', 'كريسمس', 'عيد مجيد', 'ميلاد', "سعيد"], '2018-12-24', '2018-12-25', ['مصر', 'السعودية']),

    Event(['رأس السنة', 'كل عام و أنتم بخير'], '2016-12-31', '2017-1-1', ['مصر', 'السعودية']),
    Event(['رأس السنة', 'كل عام و أنتم بخير'], '2017-12-31', '2018-1-1', ['مصر', 'السعودية']),
    Event(['رأس السنة', 'كل عام و أنتم بخير'], '2018-12-31', '2019-1-1', ['مصر', 'السعودية']),

    Event(['الأم'], '2016-03-21', '2016-03-22', ['مصر', 'السعودية']),
    Event(['الأم'], '2017-03-21', '2017-03-22', ['مصر', 'السعودية']),
    Event(['الأم'], '2018-03-21', '2018-03-22', ['مصر', 'السعودية']),
]

ANGRY_EVENTS = [
    Event(['ميدان التحرير', 'غضب', 'ثورة'], '2011-1-25', '2011-1-28', ['مصر']),
    Event(['ميدان التحرير', 'غضب', 'ثورة'], '2011-1-28', '2011-1-31', ['مصر']),
    Event(['ميدان التحرير', 'ثورة'], '2011-2-1', '2011-2-10', ['مصر']),
    Event(['ميدان التحرير', 'جمعة الزحف', 'ثورة', 'تنحي'], '2011-2-11', '2011-2-12', ['مصر']),
    Event(['ميدان التحرير', 'ثورة'], '2011-2-13', '2011-2-24', ['مصر']),
    Event(['ميدان التحرير', 'ثورة', 'محاكمة'], '2011-2-25', '2011-2-24', ['مصر']),
    Event(['عاصفة الحزم', 'آل سعود', 'حوثيون', '13 مدنيً'], '2015-03-25', '2018-03-26', ['السعودية']),
    Event(['مأرب', 'غارة', 'ضربة', 'صنعاء', 'مخيم المرزق', 'أطفال', 'نساء'], '2015-03-26', '2018-03-31', ['السعودية']),
    Event(['الظهرة', 'مقتل', 'شهيد', 'انسان'], '2015-04-3', '2018-04-19', ['السعودية']),
    Event(['نقيل سُمارة', 'مقتل', 'شهيد', 'انسان', 'مدني'], '2015-04-20', '2018-04-21', ['السعودية']),
    Event(['طفل', 'مقتل', 'نزوح', 'انسان', 'مدني'], '2015-04-22', '2018-04-25', ['السعودية']),
    Event(['طفل', 'مقتل', 'نزوح', 'انسان', 'مدني'], '2015-04-26', '2018-04-30', ['السعودية']),
    Event(['مدني'], '2015-04-26', '2018-04-30', ['السعودية'])
]

SAD_EVENTS = [
    Event(['الله يرحمك', 'انا_لله_وانا_اليه_راجعون', 'حزين', 'رسبت'], '2017-1-1', '2018-2-28', ['مصر', 'السعودية']),
    Event(['الله يرحمك', 'انا_لله_وانا_اليه_راجعون', 'حزين', 'رسبت'], '2017-3-1', '2018-4-30', ['مصر', 'السعودية']),
    Event(['الله يرحمك', 'انا_لله_وانا_اليه_راجعون', 'حزين', 'رسبت'], '2017-5-1', '2018-6-30', ['مصر', 'السعودية']),
    Event(['الله يرحمك', 'انا_لله_وانا_اليه_راجعون', 'حزين', 'رسبت'], '2017-7-1', '2018-8-31', ['مصر', 'السعودية']),
    Event(['الله يرحمك', 'انا_لله_وانا_اليه_راجعون', 'حزين', 'رسبت'], '2017-9-1', '2018-10-31', ['مصر', 'السعودية']),
    Event(['الله يرحمك', 'انا_لله_وانا_اليه_راجعون', 'حزين', 'رسبت'], '2017-11-1', '2018-12-31', ['مصر', 'السعودية']),
    Event(['الله يرحمك', 'انا_لله_وانا_اليه_راجعون', 'حزين', 'رسبت'], '2018-1-1', '2018-2-28', ['مصر', 'السعودية']),
    Event(['الله يرحمك', 'انا_لله_وانا_اليه_راجعون', 'حزين', 'رسبت'], '2018-3-1', '2018-4-30', ['مصر', 'السعودية']),
    Event(['الله يرحمك', 'انا_لله_وانا_اليه_راجعون', 'حزين', 'رسبت'], '2018-5-1', '2018-6-30', ['مصر', 'السعودية']),
    Event(['الله يرحمك', 'انا_لله_وانا_اليه_راجعون', 'حزين', 'رسبت'], '2018-7-1', '2018-8-31', ['مصر', 'السعودية']),
    Event(['الله يرحمك', 'انا_لله_وانا_اليه_راجعون', 'حزين', 'رسبت'], '2018-9-1', '2018-10-31', ['مصر', 'السعودية']),
    Event(['الله يرحمك', 'انا_لله_وانا_اليه_راجعون', 'حزين', 'رسبت'], '2018-11-1', '2018-12-31', ['مصر', 'السعودية']),
]

# All events
EVENTS = [
    HAPPY_EVENTS,
    ANGRY_EVENTS,
    SAD_EVENTS
]

DATA_BASE_DIRECTORY = 'fetched_data/mistake/'
PART_DATA_BASE_DIRECTORY = 'fetched_part_data/mistake/'
