import customtkinter as ctk

class Invoice:
    def __init__(self,poNumber,jobAddress, unitPrices, supervisor, companyEmailAddress, Company):
        self.poNumber = poNumber
        self.jobAddress = jobAddress
        self.unitPrices = unitPrices
        self.supervisor = supervisor
        self.companyEmailAddress = companyEmailAddress
        self.Company = Company

class Company:
    def __init__(self,CompanyName,companyEmailAddress,invoiceLayoutLink):
        self.Company = Company
        self.comapnyEmail = companyEmailAddress
        self.invoiceLayoutLink = invoiceLayoutLink


