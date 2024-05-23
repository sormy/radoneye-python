from typing import TypedDict


class RadonEyeStatus(TypedDict):
    serial: str
    model: str
    version: str
    latest_bq_m3: int
    latest_pci_l: float
    day_avg_bq_m3: int
    day_avg_pci_l: float
    month_avg_bq_m3: int
    month_avg_pci_l: float
    peak_bq_m3: int
    peak_pci_l: float
    counts_current: int
    counts_previous: int
    counts_str: str
    uptime_minutes: int
    uptime_str: str


class RadonEyeHistory(TypedDict):
    values_bq_m3: list[int]
    values_pci_l: list[float]
