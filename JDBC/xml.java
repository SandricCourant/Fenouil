package JDBC;
import java.util.ArrayList;

import javax.xml.parsers.*;
import javax.xml.transform.*;
import javax.xml.transform.dom.*;
import javax.xml.transform.stream.*;
import org.xml.sax.*;
import org.w3c.dom.*;
import java.io.*;

public class xml {

	public void writeXmlFile(ArrayList<Resultat> list) {

		try {

			DocumentBuilderFactory dFact = DocumentBuilderFactory.newInstance();
			DocumentBuilder build = dFact.newDocumentBuilder();
			Document doc = build.newDocument();
        
			Element root = doc.createElement("IndividuInfo");
			doc.appendChild(root);

			Element Details = doc.createElement("Details");
			root.appendChild(Details);


			for(Resultat r : list) {

				Element id = doc.createElement("idINDIVIDU");
				id.appendChild(doc.createTextNode(String.valueOf(r.getId())));
				Details.appendChild(id);
            
				Element nom = doc.createElement("nom");
				id.appendChild(doc.createTextNode(r.getNom()));
				Details.appendChild(id);
				
				Element prenom = doc.createElement("prenom");
				id.appendChild(doc.createTextNode(r.getPrenom()));
				Details.appendChild(id);
				
				Element adresse = doc.createElement("adresse");
				id.appendChild(doc.createTextNode(String.valueOf(r.getAdresse())));
				Details.appendChild(id);
				
				Element telephone = doc.createElement("telephone");
				id.appendChild(doc.createTextNode(r.getTel()));
				Details.appendChild(id);
				
				Element mail = doc.createElement("mail");
				id.appendChild(doc.createTextNode(r.getMail()));
				Details.appendChild(id);

			}


			// Save the document to the disk file
			TransformerFactory tranFactory = TransformerFactory.newInstance();
			Transformer aTransformer = tranFactory.newTransformer();

			// format the XML nicely
			aTransformer.setOutputProperty(OutputKeys.ENCODING, "ISO-8859-1");

			aTransformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "4");
			aTransformer.setOutputProperty(OutputKeys.INDENT, "yes");

			DOMSource source = new DOMSource(doc);
			try {
				FileWriter fos = new FileWriter("/home/ros.xml");
				StreamResult result = new StreamResult(fos);
				aTransformer.transform(source, result);

			} catch (IOException e) {
				e.printStackTrace();
			}
		} catch (TransformerException ex) {
			System.out.println("Error outputting document");

		} catch (ParserConfigurationException ex) {
			System.out.println("Error building document");
		}
	}
}
