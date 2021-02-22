from odoo import api, models, fields
from datetime import datetime

class projet_contact(models.Model):
    _name = 'projetprojet'
    _description = 'Nouvelle fiche projet'
    _rec_name = 'name_projet'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _inherits = {
        'res.company': 'company_id',
    }
#champ du projet
    user_id = fields.Many2one('res.users', ondelete='set null', string='Créateur du projet',default=lambda self: self.env.user)
    name_projet = fields.Text(string='Nom du projet', required=True, index=True, track_visibility="onchange")
    company_id = fields.Many2one('res.company', 'Structure partenaire', required=True, index=True, ondelete='cascade')
    type_projet1 = fields.Selection([('etatique', 'Etatique'), ('religieux', 'Religieux'),('associatif', 'Associatif'), ('autre','Autre'), ],'Type', required=True, index=True)
    date = fields.Date(string='Date début de soutient du projet', default=lambda self: fields.Date.today())
    status = fields.Selection([('Brouillon', 'brouillon'), ],'Statut', default='Brouillon', required=True, index=True)
    notes = fields.Text(string='Notes')
    name = fields.Text()
    Etapes = fields.Selection([('Nouveau', 'nouveau'), ('refuse1', 'refusé'), ('Etude', 'étude'), ('Refusé', 'refusé'), ('Validé', 'validé'), ('En cours', 'en cours'), ('Cloture', 'cloture'), ], string='Etapes', readonly=True, default='Nouveau', track_visibility="onchange")
    country_id1 = fields.Many2one('res.country', 'Pays', ondelete='cascade', required=True, index=True)
    is_document = fields.Boolean("Is Document")
    res_model = fields.Char('Resource Model', readonly=True, help="The database object this attachment will be attached to.")
    res_id = fields.Many2oneReference('Resource ID', model_field='res_model', readonly=True, help="The record id this is attached to.")
    document_new = fields.Integer()
    adresse_postale = fields.Text()
    ville = fields.Char()
    departement = fields.Char()
    description_projet = fields.Text(string='description du projet', required=True, index=True)
    code_analytique = fields.Char(track_visibility="onchange")
    budget_list_lines = fields.One2many('projetprojet.budget', 'the_budget_id', string='Budget list')
    contact_list_lines = fields.One2many('projetprojet.contact', 'the_contact_id', string='Contact list')
    event_list_lines = fields.One2many('projetprojet.event', 'the_event_id', string="Event list")
    versement_list_lines = fields.One2many('projetprojet.versement', 'the_versement_id', string='Vers list')
    evaluation_list_lines = fields.One2many('projetprojet.evaluation', 'the_evaluation_id', string='Eval list')
    materiel_list_lines = fields.One2many('projetprojet.materiel', 'the_materiel_id', string='Materiel list')
    mattechnique_list_lines = fields.One2many('projetprojet.mattechnique', 'the_mattechnique_id', string='Materiel technique liste')
    batiments_list_lines = fields.One2many('projetprojet.batiments', 'the_batiments_id', string='Batiments liste')
    beneficiaire_list_lines = fields.One2many('projetprojet.beneficiaire', 'the_beneficiaire_id', string='Beneficiaire liste')
    montant_vers_list_lines = fields.One2many('projetprojet.montant', 'the_montant_vers_id', string='Montant liste')
    inf_sensible_list_lines = fields.One2many('projetprojet.inf_sensible', 'the_inf_sensible_id', string="sensible liste")
    histoire_project = fields.Text(string="Histoire")
    tel_project = fields.Char()
    adresse_email = fields.Char()
    context_ville = fields.Text()
    context_pays = fields.Text()
    nombres_beneficiaire = fields.Integer()
    role = fields.Char(string='Nature')
    nombre = fields.Integer(string="Nombre")
    role1 = fields.Char(string='Nature')
    nombre1 = fields.Integer(string="Nombre")
    service_project = fields.Selection([('santee', 'Santé'), ('enfants', 'Enfants'), ('moyen-orient', 'Moyen-Orient'), ],'Service', track_visibility="onchange", required=True, index=True)
    annee_realisation = fields.Selection('year_selection', default="2020", string='Année début réalisation')
    zone_geographique = fields.Selection([('europe', 'Europe'), ('moyen-orient','Moyen-orient'), ('afrique','Afrique'), ('asie','Asie'), ('amerique','Amérique'), ('caraibes','Caraïbes'), ], "Zone geographique", required=True)
    champ_action = fields.Selection([('soigner','Soigner'), ('eduquer','Eduquer'), ('reinserer','Réinsérer'), ('soi_edu','Soigner et Eduquer'), ('eduq_rein','Eduquer et Réinsérer'), ('soi_rein','Réinsérer et Soigner'), ('soi_rei_edu','Soigner,Eduquer et Réinsérer'), ], string="Champ d'action", required=True, index=True)
    budget_annee_actuel = fields.Monetary(compute="get_first_line", string='Budget')
    annee_actuel = fields.Integer(default = datetime.now().year)
    localisation_geo = fields.Text(string="Localisation géographique")
    nom_resp = fields.Char(string="Nom du responsable")
    tel_resp = fields.Char(string="Téléphone du responsable")
    adresse_resp = fields.Char(string="Adresse du responsable")
    longitude = fields.Char(string="Longitude")
    latitude = fields.Char(string="Latitude")
    date_to = fields.Integer(default = datetime.now().year - 1)
    budget_annee_dernier = fields.Monetary(string="Budget", compute="get_second_line")
    annee_etude = fields.Selection('years_etude', default="étude 2020", string="Statut", required=True, index=True,  track_visibility="onchange")
    annee_encours = fields.Selection('years_encours', default="en cours 2020", string="Statut", required=True, index=True,  track_visibility="onchange")
    annee_cloture = fields.Selection([('Cloturé', 'cloturé'), ('Archivé', 'archivé'), ], default="Cloturé", string="Statut", required=True, index=True, track_visibility="onchange")
    annee_refuse = fields.Selection([('Refusé', 'refusé'), ], string="Statut", default="Refusé", required=True, index=True,  track_visibility="onchange")
    budget_test = fields.Float(string="Budget_test", compute="get_budget_verse", readonly=True)
    link_coord = fields.Char(compute='google_map_link', default="https://maps.google.com/maps")
    projet_image = fields.Image(help="Voici une présentation du projet par une photo.")
    get_verse_2020 = fields.Float(compute="verse_2020", string="total versé", readonly=True)
    get_verse_2019 = fields.Float(compute="verse_2019", string="Total versé", readonly=True)

    indirect_nbr_present = fields.Integer(compute="nbr_indirect_present", string="Indirect", readonly=True)
    direct_nbr_present = fields.Integer(compute="nbr_direct_present", string="Direct", readonly=True)
    indirect_nbr_passee = fields.Integer(compute="nbr_indirect_passee", string="Indirect", readonly=True)
    direct_nbr_passee = fields.Integer(compute="nbr_direct_passee", string="Indirect", readonly=True)

#voici les deux fonctions pour avoir le nombre de beneficiaires par annee passee
    def nbr_indirect_passee(self):
        self.indirect_nbr = 0
        for rec in self:
            for beneficiaire in rec.beneficiaire_list_lines:
                if (beneficiaire.type == "indirect" and beneficiaire.annee == str(date_to))
                    self.indirect_nbr += 1
#voici les deux fonctions pour avoir le nombre de beneficiaires par annee passee
    def nbr_direct_passee(self):
        self.direct_nbr = 0
        for rec in self:
            for beneficiaire in rec.beneficiaire_list_lines:
                if (beneficiaire.type == "direct" and beneficiaire.annee == str(date_to))
                    self.direct_nbr += 1
#voici les deux fonctions pour avoir le nombre de beneficiaires par annee actuel
    def nbr_indirect_present(self):
        self.indirect_nbr = 0
        for rec in self:
            for beneficiaire in rec.beneficiaire_list_lines:
                if (beneficiaire.type == "indirect" and beneficiaire.annee == str(annee_actuel))
                    self.indirect_nbr += 1
#voici les deux fonctions pour avoir le nombre de beneficiaires par annee actuel
    def nbr_direct_present(self):
        self.direct_nbr = 0
        for rec in self:
            for beneficiaire in rec.beneficiaire_list_lines:
                if (beneficiaire.type == "direct" and beneficiaire.annee == str(annee_actuel))
                    self.direct_nbr += 1


    def verse_2020(self):
        annee = self.annee_actuel
        annee1 = str(annee)
        self.get_verse_2020 = 0
        for rec in self:
            for versement in rec.versement_list_lines:
                if (versement.annee_vers == annee1):
                    rec.get_verse_2020 += versement.montant

    def verse_2019(self):
        annee = self.date_to
        annee1 = str(annee)
        self.get_verse_2019 = 0
        for rec in self:
            for versement in rec.versement_list_lines:
                if (versement.annee_vers == annee1):
                    rec.get_verse_2019 += versement.montant

#Permet de recuperer l'adresse du projet ou coordonner gps et de l'attribuer au champ 'link_coord'
    def google_map_link(self):
        if (self.adresse_postale):
            adrss_temp = self.adresse_postale.replace(' ','+')
        if (self.longitude and self.latitude):
            self.link_coord = 'http://maps.google.com/maps' + '?q=' + self.latitude + ',' + self.longitude
        elif (self.adresse_postale and self.departement and self.ville):
            self.link_coord = 'http://maps.google.com/maps/place/' + adrss_temp + ',+' + self.departement + '+' + self.ville
        elif (self.ville and self.adresse_postale):
            self.link_coord = 'http://maps.google.com/maps/place/' + adrss_temp + '+' + self.ville
        elif (self.ville):
            self.link_coord = 'http://maps.google.com/maps/place/' + self.ville
        else:
            self.link_coord = 'http://maps.google.com/maps'
#permet de recuperer les lignes des versements, les additioner et les attribuer au budget
    def get_budget_verse(self):
        for rec in self:
            for budget in rec.budget_list_lines:
                budget.depasser = 0
                for versement in rec.versement_list_lines:
                    if (versement.annee_vers == budget.annee):
                        budget.depasser += versement.montant
#permet de recuperer la premiere ligne pour l'attribuer au champ readonly du champ "Street"
    def get_first_line(self):
        index = 0
        temp = self.annee_actuel
        temp1 = str(temp)
        if (index < len(self.budget_list_lines) and self.budget_list_lines[index].annee == temp1 and self.budget_list_lines[index].budget_ajuste == 0):
            self.budget_annee_actuel = self.budget_list_lines[index].valider
        elif (index < len(self.budget_list_lines) and self.budget_list_lines[index].annee == temp1 and self.budget_list_lines[index].budget_ajuste != 0):
            self.budget_annee_actuel = self.budget_list_lines[index].budget_ajuste
        else:
            self.budget_annee_actuel = 0
#permet de recuperer la seconde ligne pour l'attribuer au champ readonly du champ "Street"
    def get_second_line(self):
        index = 1
        temp = self.date_to
        temp1 = str(temp)
        if (index < len(self.budget_list_lines) and self.budget_list_lines[index].annee == temp1 and self.budget_list_lines[index].budget_ajuste == 0):
            self.budget_annee_dernier = self.budget_list_lines[index].valider
        elif (index < len(self.budget_list_lines) and self.budget_list_lines[index].annee == temp1 and self.budget_list_lines[index].budget_ajuste != 0):
            self.budget_annee_dernier = self.budget_list_lines[index].budget_ajuste
        elif (0 < len(self.budget_list_lines) and self.budget_list_lines[0].annee == temp1 and self.budget_list_lines[0].budget_ajuste == 0):
            self.budget_annee_dernier = self.budget_list_lines[0].valider
        elif (0 < len(self.budget_list_lines) and self.budget_list_lines[0].annee == temp1 and self.budget_list_lines[0].budget_ajuste != 0):
            self.budget_annee_dernier = self.budget_list_lines[0].budget_ajuste
        else:
            self.budget_annee_dernier = 0
#permet de changer d'etapes
    def action_etude(self):
        for rec in self:
            rec.Etapes = 'Etude'
#permet de retourner en arriere dans les etapes
    def action_admin(self):
        for rec in self:
            if (rec.Etapes == 'Etude'):
                rec.Etapes = 'Nouveau'
            if (rec.Etapes == 'refuse1'):
                rec.Etapes = 'Nouveau'
            if (rec.Etapes == 'Refusé'):
                rec.Etapes = 'Etude'
            if (rec.Etapes == 'Validé'):
                rec.Etapes = 'Etude'
            if (rec.Etapes == 'Cloture'):
                rec.Etapes = 'Validé'
#permet de changer d'etapes
    def action_valider(self):
        for rec in self:
            rec.Etapes = 'Validé'
    def action_refuser(self):
        for rec in self:
            rec.Etapes = 'Refusé'
    def action_refuse(self):
        for rec in self:
            rec.Etapes = 'refuse1'
    def action_encour(self):
        for rec in self:
            rec.Etapes = 'En cours'
    def action_cloture(self):
        for rec in self:
            rec.Etapes = 'Cloture'
    @api.onchange('state_id')
    def onchange_state(self):
        if self.state_id:
            self.country_id = self.state_id.country_id.id
#permet de choisir une annee de 2000 a 2100
    def year_selection(self):
        year = 2000
        year_list = []
        year1 = "1970-1980"
        year2 = "1980-1990"
        year3 = "1990-2000"
        year_list.append((year1, year1))
        year_list.append((year2, year2))
        year_list.append((year3, year3))
        while year != 2100:
            year_list.append((str(year), str(year)))
            year += 1
        return year_list
#permet de choisir une annee de 2000 a 2026 pour l etape etude
    def years_etude(self):
        year = 2020
        etude = "étude "
        year_list = []
        while year != 2026:
            result = etude + str(year)
            year_list.append((result, result))
            year += 1
        return year_list
#permet de choisir une annee de 2000 a 2026 pour l'etape en cours
    def years_encours(self):
        year = 2020
        etude = "en cours "
        year_list = []
        year_list.append((str("reporté"), str("reporté")))
        while year != 2026:
            result = etude + str(year)
            year_list.append((result, result))
            year += 1
        return year_list
#permet d inherit les models et attribuer le domain et context au projet
class parent_projet(models.Model):
        _inherit ="res.partner"
        _inherit ="res.users"
        _inherit ="res.country"
        _inherit = "ir.attachment"

        def action_projet_button(self):
            action = self.env.ref('projet_projet.action_projet_button').read()[0]
            action['domain'] = [('projet_id','=',self.id)]
            action['context']= {'default_projet_id':self.id}
            return action
#permet de gerer le tableau des contacts
class contact_list(models.Model):
        _name = 'projetprojet.contact'
        _description = 'contact liste'

        begin_date = fields.Date(string='Date de début', default=lambda self: fields.Date.today())
        contact_represent1 = fields.Selection([('représentant', 'Représentant'), ('conseiller medical', 'Conseiller médical'), ('partenaires financiers', 'Partenaires financiers'), ('partenaires technique','Partenaires techniques'), ], string='Rôle')
        organisation = fields.Many2one('res.company', ondelete='set null', string='Organisation')
        the_contact_id = fields.Many2one('projetprojet', ondelete='set null', string='Fiche contact')
        the_contact_id1 = fields.Many2one('res.partner', ondelete='set null', string='Fiche contact', default=lambda self: self.env.user)
        end_date = fields.Date(string='Date de fin')
        afrique = fields.Char(string="Afrique")
#permet de gerer le tableau des versements
class versement_list(models.Model):
        _name = 'projetprojet.versement'
        _description = 'versement liste'
        _order = "date desc"

        the_versement_id = fields.Many2one('projetprojet', ondelete='set null', string='Fiche versement')
        currency_id = fields.Many2one('res.currency', ondelete='set null', string='Currency')
        date = fields.Date(string='Date de versement')
        montant = fields.Float(string='Montant')
        object = fields.Char(string='Motif')
        annee_vers = fields.Selection('year_selection', default="2020", string="Année par versement")
        Ligne_budgetaire = fields.Selection('ilep', string="Ligne budgétaire")

        @api.model
#permet de selectionner une annee de 2000 a 2099
        def year_selection(self):
            year = 2000
            year_list = []
            while year != 2100:
                year_list.append((str(year), str(year)))
                year += 1
            return year_list
#fonction qui permet de choisir un nombre entre 11 et 46 pour les codes ilep
        def ilep(self):
            ilep = 11
            ilep_list = []
            while ilep != 47:
                ilep_list.append((str(ilep), str(ilep)))
                ilep += 1
            return ilep_list
#permet de gerer le deuxieme tableau dans l'onglet versement
class montant_vers_list(models.Model):
        _name = 'projetprojet.montant'
        _description = 'montant verse par lignes budgetaire'

        the_montant_vers_id = fields.Many2one('projetprojet', ondelete='set null', string='Fiche montant versé')
        total_verse = fields.Integer(string="Total versé")
        annee = fields.Selection('year_selection', default="2020", string="Année")
        ligne_budgetaire = fields.Selection('ilep', string="Ligne budgétaire")

        def year_selection(self):
            year = 2000
            year_list = []
            while year != 2100:
                year_list.append((str(year), str(year)))
                year += 1
            return year_list
        def ilep(self):
            ilep = 11
            ilep_list = []
            while ilep != 47:
                ilep_list.append((str(ilep), str(ilep)))
                ilep += 1
            return ilep_list
#permet de gerer le tableau des budget
class budget_list(models.Model):
        _name = 'projetprojet.budget'
        _description = 'budget liste'
        _order = "annee desc"

        the_budget_id = fields.Many2one('projetprojet', ondelete='set null', string='Fiche budget')
        currency_id = fields.Many2one('res.currency', ondelete='set null', string='Currency')
        commission_date = fields.Date(string='Date de validation')
        annee = fields.Selection('year_selection', default="2020", string='Année budgetaire')
        demande = fields.Monetary(string='Demande partenaire')
        zone_text = fields.Text(string='Détails')
        budget_ajuste = fields.Monetary(string="Budget ajusté")
        valider = fields.Monetary(string="Budget validé")
        depasser = fields.Float(compute='sql_query', default="0", string="Versé", readonly=True)
        def sql_query(self):
            self.depasser = 0
            self._cr.execute("select SUM(montant) from projetprojet_budget JOIN projetprojet_versement ON projetprojet_versement.annee_vers = projetprojet_budget.annee and projetprojet_versement.the_versement_id = projetprojet_budget.the_budget_id")

#permet de selectioner une annee de  2000 a 2099
        def year_selection(self):
            year = 2000
            year_list = []
            while year != 2100:
                year_list.append((str(year), str(year)))
                year += 1
            return year_list
#permet de gerer le tableau des evenements
class event_list(models.Model):
        _name = 'projetprojet.event'
        _description = 'event liste'
        _order = "date_debut desc"

        the_event_id = fields.Many2one('projetprojet', ondelete='set null', string='Liste event')
        type_passage1 = fields.Selection([('visite', 'Visite'), ('ceremonie', 'Cérémonie'), ('activite', 'Activité'), ('incident', 'Incident'), ('autre','Autre'), ], string='Type')
        date_debut = fields.Date(string='Date de début')
        date_fin = fields.Date(string="Date de fin")
        description = fields.Text(string='Description')
        type_event = fields.Selection([('interne','Interne'), ('externe','Externe'), ], string="Catégorie")
        object = fields.Char(string="Objet")

#    def cal_jours(self):
#        datetime.now().year - datetime.now(year) - 1

#permet de gerer le tableau des evaluations
class evaluation_list(models.Model):
        _name = 'projetprojet.evaluation'
        _description = 'evaluation liste'

        the_evaluation_id = fields.Many2one('projetprojet', ondelete='set null', string='Fiche evaluation')
        annee = fields.Selection('year_selection', default="2020", string='Année')
        objectif_fixer = fields.Text(string='Objectifs fixés')
        evaluation_milieu = fields.Text(string='Evaluation Milieu/Année')
        evaluation_fin = fields.Text(string='Evaluation Fin/Année')
        resultat_evaluation = fields.Text(string='Resultat Evaluation')
#permet de choisir une annee de 2000 a 2099
        @api.model
        def year_selection(self):
            year = 2000
            year_list = []
            while year != 2100:
                year_list.append((str(year), str(year)))
                year += 1
            return year_list
#permet de gerer le tableau du materiel roulant dans inventaire
class materiel_list(models.Model):
    _name = 'projetprojet.materiel'
    _description = 'materiel liste'

    the_materiel_id = fields.Many2one('projetprojet', ondelete='set null', string='Fiche materiel')
    date_aqui = fields.Date(string="Date d'aquisition")
    vehicule = fields.Char()
    type_vehicule1 = fields.Selection([('moto', 'Moto'), ('auto', 'Auto'), ], string='Type')
    Immatriculation = fields.Char()
    etat1 = fields.Selection([('neuf', 'Neuf'), ('bon', 'Bon'), ('moyen', 'Moyen'), ('mauvais', 'Mauvais'), ], string='Etat')
    kilometrages = fields.Integer(string="Kilométrages")
    date_kilo = fields.Date(string="Date dernier relevé kilométrique")
    date_session = fields.Date(string="Date de cession")
    prix_session = fields.Integer(string="Prix de cession")
    acheteur = fields.Char(string="Acheteur")
    entretien = fields.Date(string="Date de l'entretien technique")
    commentaires = fields.Char(string="Commentaires")
#permet de gerer le tableau du materiel technique dans inventaire
class materiel_tech(models.Model):
    _name = 'projetprojet.mattechnique'
    _description = 'materiel technique liste'

    the_mattechnique_id = fields.Many2one('projetprojet', ondelete='set null', string='Fiche materiel technique')
    date_aqui = fields.Date(string="Date d'aquisition")
    etat1 = fields.Selection([('neuf', 'Neuf'), ('bon', 'Bon'), ('moyen', 'Moyen'), ('mauvais', 'Mauvais'), ], string='Etat')
    type_materiel1 = fields.Selection([('informatique', 'Informatique'), ('mobilier', 'Mobilier'), ('bureaucratique', 'Bureaucratique'), ('betails','Bétails'), ('autre','Autre'), ], string='Type')
    nombre = fields.Integer()
    nom = fields.Char()
#permet de gerer le tableau des batiments dans inventaire
class batiments_list(models.Model):
    _name = 'projetprojet.batiments'
    _description = 'batiment liste'

    the_batiments_id = fields.Many2one('projetprojet', ondelete='set null', string='Fiche batiments')
    date_aqui = fields.Date(string="Date d'aquisition ou de construction")
    etat1 = fields.Selection([('neuf', 'Neuf'), ('bon', 'Bon'), ('moyen', 'Moyen'), ('mauvais', 'Mauvais'), ], string='Etat')
    fonction1 = fields.Selection([('soins', 'Soins'), ('logement', 'Logement'), ('bureau', 'Bureau'), ('commerce','Commerce'), ('autre', 'Autre'), ], string='Fonction')
    couts_achat = fields.Integer("Couts d'achat ou de construction")
    nature = fields.Selection([('construction','Construction'),('aquisition','Aquisition'), ], string ="Nature")
#permet de gerer le tableau beneficiaires dans beneficiaires
class beneficiaire_list(models.Model):
    _name = 'projetprojet.beneficiaire'
    _description = 'beneficiaire liste'

    the_beneficiaire_id = fields.Many2one('projetprojet', ondelete='set null', string='Fiche contact')
    the_contact_id = fields.Many2one('res.partner', ondelete='set null', string='Nom des bénéficiaires')
    annee = fields.Selection('year_selection', default="2020", string='Année')
    activite = fields.Char(string="Activité")
    nombre = fields.Char(default="inconnu", string="Nombre")
    type = fields.Selection([('Direct', 'direct'), ('Indirect', 'indirect'),], string='Type')
    nature = fields.Char(string="Nature")
    champ_action = fields.Selection([('soigner','Soigner'), ('eduquer','Eduquer'),('reinserer','Réinsérer'), ], string="Champs d'action")
#permet de choisir un nombre entre 2000 et 2099
    @api.model
    def year_selection(self):
        year = 2000
        year_list = []
        while year != 2100:
            year_list.append((str(year), str(year)))
            year += 1
        return year_list
class beneficiaire_list(models.Model):
    _name = 'projetprojet.inf_sensible'
    _description = 'Informations sensible'
    _order = "date desc"

    the_inf_sensible_id = fields.Many2one('projetprojet', ondelete='set null', string='Fiche sensible')
    date = fields.Date(string="Date")
    sujet = fields.Char(string="Sujet")
    details = fields.Text(string="Détails")
    type = fields.Selection([('direct', 'Direct'), ('indirect', 'Indirect'),], string='Type')
    nature = fields.Char(string="Nature")
    annee = fields.Selection("year_selection", string="Année")

#permet de choisir un nombre entre 2000 et 2099
    @api.model
    def year_selection(self):
        year = 1980
        year_list = []
        while year != 2100:
            year_list.append((str(year), str(year)))
            year += 1
        return year_list