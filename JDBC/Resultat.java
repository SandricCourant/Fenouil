package JDBC;

public class Resultat {
	private int id;
	private String nom;
	private String prenom;
	private int adresse;
	private String tel;
	private String mail;
	public Resultat(int id, String nom, String prenom, int adresse, String tel, String mail) {
		this.id = id;
		this.nom = nom;
		this.prenom = prenom;
		this.adresse = adresse;
		this.tel = tel;
		this.mail = mail;
	}
	public int getId() {
		return id;
	}
	public String getNom() {
		return nom;
	}
	public String getPrenom() {
		return prenom;
	}
	public int getAdresse() {
		return adresse;
	}
	public String getTel() {
		return tel;
	}
	public String getMail() {
		return mail;
	}
	
	
}
