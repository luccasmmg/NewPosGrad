#!/usr/bin/env python3

from pydantic import BaseModel, HttpUrl, PositiveInt

from app.db.models import DocumentCategory, Rank

import typing as t

import datetime

class ResearcherBase(BaseModel):
    cpf: str
    name: str

class ResearcherCreate(ResearcherBase):
    pass

class ResearcherEdit(ResearcherBase):
    pass

class Researcher(ResearcherBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

#Student advisor

class StudentAdvisorBase(BaseModel):
    registration: int
    advisor_name: str

class StudentAdvisorCreate(StudentAdvisorBase):
    pass

class StudentAdvisorEdit(StudentAdvisorBase):
    pass

class StudentAdvisor(StudentAdvisorBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

#Covenant schemas

class CovenantBase(BaseModel):
    name: str
    initials: str

class CovenantCreate(CovenantBase):
    logo_file: str
    pass

class CovenantEdit(CovenantBase):
    pass

class Covenant(CovenantBase):
    logo_file: str
    id: int
    owner_id: int

    class Config:
        orm_mode = True

#Participation schemas

class ParticipationBase(BaseModel):
    title: str
    description: str = ""
    year: PositiveInt = None
    international: bool = False

class ParticipationCreate(ParticipationBase):
    pass

class ParticipationEdit(ParticipationBase):
    pass

class Participation(ParticipationBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

#Official Document

class OfficialDocumentBase(BaseModel):
    title: str
    cod: str
    category: DocumentCategory

class OfficialDocumentCreate(OfficialDocumentBase):
    file: str
    pass

class OfficialDocumentEdit(OfficialDocumentBase):
    pass

class OfficialDocument(OfficialDocumentBase):
    id: int
    owner_id: int
    inserted_on: datetime.datetime
    file: str

    class Config:
        orm_mode = True

#Staff

class StaffBase(BaseModel):
    name: str
    rank: Rank
    description: str

class StaffCreate(StaffBase):
    photo: str
    pass

class StaffEdit(StaffBase):
    pass

class Staff(StaffBase):
    id: int
    owner_id: int
    photo: str

    class Config:
        orm_mode = True

#News

class NewsBase(BaseModel):
    title: str
    headline: str
    date: datetime.date
    body: str

class NewsCreate(NewsBase):
    pass

class NewsEdit(NewsBase):
    pass

class News(NewsBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

#Event

class EventBase(BaseModel):
    title: str
    link: HttpUrl
    initial_date: datetime.datetime
    final_date: datetime.datetime

class EventCreate(EventBase):
    pass

class EventEdit(EventBase):
    pass

class Event(EventBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

#ScheduledReport

class ScheduledReportBase(BaseModel):
    title: str
    author: str
    location: str
    datetime: datetime.datetime

class ScheduledReportCreate(ScheduledReportBase):
    pass

class ScheduledReportEdit(ScheduledReportBase):
    pass

class ScheduledReport(ScheduledReportBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
