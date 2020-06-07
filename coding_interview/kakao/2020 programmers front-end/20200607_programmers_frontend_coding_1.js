// const days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
const days = [
  0, 31, 59, 90,
  120, 151, 181, 212, 243,
  273, 304, 334, 365];
const offers = [
  '10/05 10/12 2400',
  '10/05 10/10 2500',
  '10/07 10/15 2300',
  '10/08 10/30 3000',
  '10/15 11/03 3000',
  '10/20 11/01 3500',
  '11/02 11/11 4000',
];

const offers2 = [
  '07/01 07/30 2000',
  '07/01 07/15 2000',
  '07/01 07/30 2000',
  '07/01 07/30 1500',
  '07/05 07/30 2100',
  '07/20 08/01 2400',
  '07/20 07/31 2400',
  '07/31 09/01 2900',
  '08/01 08/15 3000',
  '08/14 08/19 2000',
  '08/17 08/30 4000'];
const offers3 = [];
function solution(offers) {
  const parsedOffers = offers.map(offer => {
    const [s, e, salary] = offer.split(' ');
    const [start_month, start_day] = s.split('/').map(v => parseInt(v));
    const start = days[start_month - 1] + start_day;

    const [end_month, end_day] = e.split('/').map(v => parseInt(v));
    const end = days[end_month - 1] + end_day;

    return [start, end, salary];
  });

  const offer_dic = {};
  const start_days = [];
  parsedOffers.forEach(([start, end, salary]) => {
    start_days.push(start);
    if (!(start in offer_dic)) {
      offer_dic[start] = [];
    }
    offer_dic[start].push([end, parseInt(salary)]);
  });
  const start_set = new Set(start_days.sort());

  let current_salary = 0;
  let current_endday = 366;
  for (const start of start_set) {
    if (start > current_endday) return current_salary;

    const offers = offer_dic[start];
    for (const [end, salary] of offers) {
      if ((salary > current_salary) ||
          (salary === current_salary && end > current_endday)) {
        current_salary = salary;
        current_endday = end;
      }

    }
  }

  return current_salary;
}

console.log(solution(offers));
console.log(solution(offers2));
console.log(solution(offers3));
