import 'dart:async';

void main() async {
  pomodoro(4, 25, 5);
}

void timer(int minute) {
  var counter = minute * 60;
  var minuteTimer = counter;
  Timer.periodic(const Duration(seconds: 1), (timer) {
    var now = minuteTimer - timer.tick;
    print('${now~/60}:${now%60}');
    counter--;
    if (counter == 0) {
      timer.cancel();
    }
  });
}


Future<void> set_of_timer(int work_time, int rest_time) async {
  print('작업 시간이 시작되었습니다.');
  timer(work_time);
  await Future.delayed(Duration(milliseconds: work_time*1000*60 + 5));
  print('작업 시간이 종료되었습니다. 휴식 시간을 시작합니다.');
  timer(rest_time);
  await Future.delayed(Duration(milliseconds: rest_time*1000*60 + 5));
  print('휴식 시간이 종료되었습니다.');
}

Future<void> pomodoro(int repeat, int work_time, int rest_time) async {
  for (repeat; repeat > 0; repeat--){
    if (repeat == 1) {
      set_of_timer(work_time, rest_time+10);
    }
    else {
      set_of_timer(work_time, rest_time);
      await Future.delayed(Duration(milliseconds: (work_time+rest_time)*1000*60 + 30 + repeat));
    }
  }
}
