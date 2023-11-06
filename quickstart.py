""" Quickstart script for InstaPy usage """

# imports
from srt_reservation.main import SRT
from srt_reservation.util import parse_cli_args


if __name__ == "__main__":
    cli_args = parse_cli_args()

    login_id = "$id"
    login_psw = "$psw"
    dpt_stn = "수서"
    arr_stn = "동탄"
    dpt_dt = "20231114"
    dpt_tm = "18" # should be even number 짝수

    order_trains_to_check = [1,3,5] # order of trains to reserve 몇번째 기차 예매할지
    want_reserve = True # ignore it

    srt = SRT(dpt_stn, arr_stn, dpt_dt, dpt_tm, order_trains_to_check, want_reserve)
    srt.run(login_id, login_psw)