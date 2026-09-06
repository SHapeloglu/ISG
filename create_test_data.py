#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
F5-003 HSE Radar Acceptance Test — Sample Data Creator
Çalıştırma: python3 create_test_data.py
"""

import os
import sys
import django

# Odoo setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "odoo.settings")
sys.path.insert(0, '/opt/odoo/odoo18')
sys.path.insert(0, '/opt/odoo/isg_addons')

import odoo
from odoo import api, SUPERUSER_ID

def create_test_data():
    """Create minimal test data for F5-003 acceptance test"""
    
    with odoo.api.Environment.manage():
        env = api.Environment(odoo.sql_db.db_connect('isg').cursor(), SUPERUSER_ID, {})
        
        print("[*] Creating test data...")
        
        # 1. Workplace
        print("  [1] Workplace...")
        company = env.ref('base.main_company')
        workplace = env['isg.workplace'].create({
            'name': 'Test Facility - Acceptance Test',
            'company_id': company.id,
            'danger_class': 'high',
            'nace_code': '2511',
            'sgk_workplace_code': 'TEST-999-001',
        })
        print(f"      ✓ Workplace: {workplace.name} (ID: {workplace.id})")
        
        # 2. Site
        print("  [2] Site...")
        site = env['isg.site'].create({
            'name': 'Main Workshop',
            'workplace_id': workplace.id,
        })
        print(f"      ✓ Site: {site.name}")
        
        # 3. Employee
        print("  [3] Employee...")
        employee = env['hr.employee'].create({
            'name': 'Test Worker',
            'isg_workplace_id': workplace.id,
            'isg_site_id': site.id,
        })
        print(f"      ✓ Employee: {employee.name}")
        
        # 4. Risk Assessment
        print("  [4] Risk Assessment...")
        risk = env['isg.risk.assessment'].create({
            'name': 'Test Risk Assessment',
            'workplace_id': workplace.id,
            'company_id': company.id,
            'assessment_type': 'initial',
            'team_leader_id': employee.id,
        })
        print(f"      ✓ Risk: {risk.name}")
        
        # 5. Incident
        print("  [5] Incident...")
        incident = env['isg.incident'].create({
            'name': 'Test Incident - Cut',
            'workplace_id': workplace.id,
            'incident_date': env['fields'].Date.today(),
            'incident_type': 'accident',
            'injury_type': 'cut',
            'injured_employee_id': employee.id,
        })
        print(f"      ✓ Incident: {incident.name}")
        
        # 6. Audit
        print("  [6] Audit...")
        audit = env['isg.audit'].create({
            'name': 'Test Audit - Initial',
            'workplace_id': workplace.id,
            'audit_date': env['fields'].Date.today(),
            'audit_type': 'internal',
        })
        print(f"      ✓ Audit: {audit.name}")
        
        # 7. Equipment Inspection
        print("  [7] Equipment...")
        eq_type = env['isg.equipment.type'].create({
            'name': 'Test Forklift',
            'ek_ii_category': 'lifting_equipment',
            'inspection_period_months': 6,
        })
        equipment = env['isg.equipment'].create({
            'name': 'Forklift #TEST-001',
            'equipment_type_id': eq_type.id,
            'workplace_id': workplace.id,
            'serial_number': 'TEST-001-2026',
            'manufacturer': 'Test Inc',
            'model': 'T-1000',
        })
        inspection = env['isg.equipment.inspection'].create({
            'equipment_id': equipment.id,
            'inspection_date': env['fields'].Date.today(),
            'result': 'compliant',
        })
        print(f"      ✓ Equipment: {equipment.name}")
        print(f"      ✓ Inspection: {inspection.id}")
        
        # 8. PTW + LOTO
        print("  [8] PTW + LOTO...")
        ptw_type = env['isg.ptw.type'].create({
            'name': 'Test Hot Work',
            'code': 'test_hot_work',
            'description': 'Testing hot work permit',
            'default_validity_hours': 8,
        })
        ptw = env['isg.ptw'].create({
            'ptw_type_id': ptw_type.id,
            'workplace_id': workplace.id,
            'work_description': 'Test welding job',
            'work_date': env['fields'].Date.today(),
            'work_start_time': '08:00',
            'work_end_time': '17:00',
            'requester_id': employee.id,
        })
        loto = env['isg.loto'].create({
            'permit_id': ptw.id,
            'energy_source': 'Main Power Panel',
            'isolation_point': 'Circuit Breaker A',
            'lock_device': 'Padlock #001',
            'locked_by': employee.id,
        })
        print(f"      ✓ PTW: {ptw.name}")
        print(f"      ✓ LOTO: {loto.id}")
        
        print("\n[✓] Test data created successfully!")
        print(f"\nCreated:")
        print(f"  • Workplace: {workplace.id}")
        print(f"  • Site: {site.id}")
        print(f"  • Employee: {employee.id}")
        print(f"  • Risk: {risk.id}")
        print(f"  • Incident: {incident.id}")
        print(f"  • Audit: {audit.id}")
        print(f"  • Equipment: {equipment.id}")
        print(f"  • PTW: {ptw.id}")
        
        env.cr.commit()

if __name__ == '__main__':
    create_test_data()
