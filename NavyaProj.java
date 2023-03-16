import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class NavyaProj {

	public static void main(String[] args) throws FileNotFoundException {
		Scanner sc = new Scanner(System.in);
		String fileInput = sc.next();
		String city1 = sc.next();
		String city2 = sc.next();
		String heuristicfile = sc.next();
		//System.out.println(heuristicfile);
		List<String> nodes_visit = new ArrayList<>();
		List<HashMap<String, String>> list_final = new ArrayList<>();
		List<HashMap<String, String>> queue = new ArrayList<>();
		List<HashMap<String, String>> route_travelled = new ArrayList<>();
		HashMap<String,String> heuristics_values = new HashMap();
		
		int node_expand=0, node_generate=1, node_pop=0;
		Scanner filescanner = new Scanner(new File(System.getProperty("user.dir")+File.separator+fileInput));
		//System.out.println(filescanner.nextLine());
		while(filescanner.hasNextLine()) {
			String line = filescanner.nextLine().trim();
			if(line.equalsIgnoreCase("END OF INPUT"))
				break;
			else {
				String h[] = line.split(" ");
				HashMap<String,String> map = new HashMap();
				map.put("city1", h[0]);
				map.put("city2", h[1]);
				map.put("cost", h[2]);
				route_travelled.add(map);
			}
			
		}
		filescanner.close();
		//System.out.println(route_travelled.get(3));
		if(!heuristicfile.equalsIgnoreCase("NA")) {
			Scanner filescanner2 = new Scanner(new File(System.getProperty("user.dir")+File.separator+heuristicfile));
			while(filescanner2.hasNextLine()) {
				String line2 = filescanner2.nextLine().trim();
				//System.out.println(line2);
				if(line2.equalsIgnoreCase("END OF INPUT"))
					break;
				else {
					String h[] = line2.split(" ");
					
					heuristics_values.put(h[0], h[1]);
				}
			}
			filescanner2.close();
		}
		//System.out.println(heuristics_values.get(5));
		HashMap<String,String> rt_node = new HashMap();
		rt_node.put("city_one", city1);
		rt_node.put("parent", "");
		rt_node.put("cost", "0");
		rt_node.put("pt_costs", "0");
		rt_node.put("heuristic_cost", "0");
		rt_node.put("dp", "0");
		queue.add(rt_node);
		list_final.add(rt_node);
		//System.out.println(queue.size());
		//System.out.println(list_final);
		while(queue.size()>0) {
			Collections.sort(queue, mapComparator);
			//System.out.println(queue);
			HashMap<String,String> cheapest_node = new HashMap();
			cheapest_node = queue.get(0);
			//System.out.println(cheapest_node);
			queue.remove(0);
			node_pop++;
			if(cheapest_node.get("city_one").equalsIgnoreCase(city2)) {
				//System.out.println("Yaha");
				List<String> res = new ArrayList<>();
				String pt = cheapest_node.get("parent");
				res.add(pt + " to " + city2 + "," + String.valueOf(cheapest_node.get("pt_costs"))+ " km");
				System.out.println("Nodes popped:" + String.valueOf(node_pop) +"\n Nodes expanded:" + 
						String.valueOf(node_expand) + "\n Nodes generated:" + String.valueOf(node_generate) + "\n Distance:" + String.valueOf(cheapest_node.get("cost")) + " km" + "\n Route:");
				while(pt!="") {
					for(HashMap<String, String> list:list_final) {
						if(list.get("city_one").equalsIgnoreCase(pt)) {
							pt=list.get("parent");
							if(pt!="")
								res.add(pt+" to " + list.get("city_one")+ ", " + list.get("pt_costs") + " km");
							break;
						}
					}
				}
				Collections.reverse(res);
				for(String c:res) {
					System.out.println(c);
				}
				break;
			}
			if(nodes_visit.contains(cheapest_node.get("city_one")))
				continue;
			else {
				String current_city="";
				for(HashMap<String, String> list:route_travelled) {
					//System.out.println("Loop k andar");
					String city1_city = list.get("city1");
					String destination_city = list.get("city2");
					current_city = cheapest_node.get("city_one");
					String city_one ="";
					if (current_city.equalsIgnoreCase(city1_city) || current_city.equalsIgnoreCase(destination_city)) {
						//System.out.println("Let's see");
						float heuristic_cost=0;
		                if (current_city.equalsIgnoreCase(city1_city)) {
		                   city_one = destination_city;
		                }
		                else {
		                	city_one = city1_city;
		                }
		                if(heuristics_values.size()>0) {
		                	heuristic_cost=Float.parseFloat(heuristics_values.get(city_one));
		                }
		                HashMap<String,String> var = new HashMap();
		                var.put("city_one", city_one);
		                var.put("parent", cheapest_node.get("city_one"));
		                var.put("pt_costs", list.get("cost"));
		                var.put("cost", String.valueOf(Float.parseFloat(cheapest_node.get("cost"))+Float.parseFloat(list.get("cost"))));
		                var.put("heuristic_cost", String.valueOf(Float.parseFloat(cheapest_node.get("cost"))+Float.parseFloat(list.get("cost"))+heuristic_cost));
		                var.put("dp", String.valueOf(Float.parseFloat(cheapest_node.get("cost"))+1));
		                //System.out.println(var);
		                queue.add(var);
		                //System.out.println(queue.size());
		                list_final.add(var);
		                node_generate++;
					}
				}
				node_expand++;
				nodes_visit.add(current_city);
				//System.out.println(queue.size());
			}
				
		}
		if(queue.size()==0) {
			System.out.println("Nodes popped:" + node_pop + "\n Nodes expanded:" + node_expand + "\n Nodes generated:" + node_generate + "\n Distance:" + " Infinity" + "\n Route: \n None");
		}
		

	}
	public static Comparator<Map<String, String>> mapComparator = new Comparator<Map<String, String>>() {
	    public int compare(Map<String, String> m1, Map<String, String> m2) {
	        return Float.compare(Float.parseFloat(m1.get("heuristic_cost")),(Float.parseFloat(m2.get("heuristic_cost"))));
	    }
	};

}
