import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')
django.setup()

from main.models import Blog, Category
from django.contrib.auth.models import User

def seed():
    print("🚀 Populating CORE with deep-dive technical documentation...")
    Blog.objects.all().delete()
    
    user = User.objects.first() or User.objects.create_superuser('admin', 'admin@test.com', 'admin123')
    arch, _ = Category.objects.get_or_create(name="Architecture")
    eng, _ = Category.objects.get_or_create(name="Engineering")

    posts = [
        {
            "title": "Sustainable Urban Skyscrapers",
            "cat": arch,
            "image": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1000",
            "content": (
                "The evolution of the skyscraper is no longer defined by height, but by environmental integration. "
                "In the 20th century, skyscrapers were energy-hungry monoliths of steel and glass. Today, they are "
                "reimagined as vertical ecosystems that generate more power than they consume through integrated "
                "photovoltaic glass and high-altitude wind turbines.\n\n"
                "One of the primary challenges in high-rise sustainability is the 'Heat Island' effect, where buildings "
                "trap heat in urban canyons. Engineers are countering this through 'Living Walls'—massive vertical gardens "
                "that provide natural insulation. These biological layers reduce internal cooling costs by 30% and "
                "significantly improve urban air quality for the surrounding community.\n\n"
                "Water management within these structures has also reached new levels of sophistication. Closed-loop "
                "greywater systems harvest rainwater from the roof and process it through bio-filters for irrigation "
                "and plumbing. This reduces municipal water demand by up to 60%, making the building a self-sustaining "
                "node in the city's infrastructure.\n\n"
                "The transition to mass timber in high-rise construction is perhaps the most revolutionary shift. "
                "Cross-Laminated Timber (CLT) allows for carbon sequestration within the structural frame itself. "
                "Recent projects have proven that timber-hybrid structures can achieve the same fire safety ratings "
                "as concrete while being significantly lighter and faster to assemble.\n\n"
                "Technological integration via IoT sensors allows for real-time adjustments to a building's 'breathing' "
                "patterns. Smart windows tint automatically to manage solar gain, while AI-driven ventilation systems "
                "optimize airflow based on occupancy. This reduces energy waste during off-peak hours by nearly 40%.\n\n"
                "As we look toward 2030, the skyscraper is becoming a tool for urban repair. Future designs "
                "incorporate vertical farming and carbon-scrubbing facades, transforming these structures from "
                "passive shelters into active participants in the fight against climate change."
            )
        },
        {
            "title": "Biophilic Design in Workspaces",
            "cat": arch,
            "image": "https://images.unsplash.com/photo-1597047084897-51e81819a499?q=80&w=1000",
            "content": (
                "Biophilic design is a strategic approach that taps into the innate human connection to nature. "
                "In modern workspace engineering, this is not just about aesthetics; it is about cognitive performance. "
                "Environments incorporating natural light and organic materials can reduce employee stress levels "
                "by 15% and increase overall focus and productivity.\n\n"
                "The core principles involve 'Direct Experience of Nature,' such as indoor water features that provide "
                "acoustic masking. This white noise helps drown out distractions in open-plan offices while providing "
                "a calming sensory experience. The presence of water has been linked to lower heart rates and "
                "improved creative problem-solving capabilities.\n\n"
                "Indirect experiences use earth tones and natural curvatures instead of harsh, straight lines. "
                "The use of 'Fractal Patterns'—the repeating patterns found in leaves and coastlines—has been "
                "proven to reduce mental fatigue. By mimicking these natural geometries in carpets and wall textures, "
                "designers can create a sense of comfort in otherwise artificial environments.\n\n"
                "Natural ventilation systems that mimic outdoor airflow variability also play a crucial role. "
                "Traditional HVAC systems often lead to 'Sick Building Syndrome' due to stagnant air. Modern "
                "biophilic offices use wind-catchers and thermal chimneys to ensure a constant supply of "
                "fresh, oxygen-rich air throughout the day.\n\n"
                "Lighting is another critical engineering pillar. Circadian lighting systems adjust color temperatures "
                "throughout the day to match the natural movement of the sun. This regulates the occupants' "
                "internal clocks, improving sleep quality at home and alertness during the 9-to-5 window.\n\n"
                "The long-term benefits of this holistic approach are undeniable. Companies that invest in biophilic "
                "upgrades see a measurable decrease in absenteeism and a surge in employee retention. The built "
                "environment is no longer just a shell; it is a biological support system for the human mind."
            )
        },
        {
            "title": "The Mechanics of Modern Bridges",
            "cat": eng,
            "image": "https://images.unsplash.com/photo-1449034446853-66c86144b0ad?q=80&w=1000",
            "content": (
                "Modern bridge engineering is defined by the quest for longer spans and thinner profiles. "
                "Cable-stayed bridges have become the preferred choice for medium-to-long distances, utilizing "
                "Ultra-High Performance Concrete (UHPC). This material possesses compressive strengths "
                "exceeding 20,000 psi, allowing for lighter and more durable deck segments.\n\n"
                "Structural health monitoring has been revolutionized by the integration of 'Digital Twins.' "
                "By embedding fiber-optic sensors and accelerometers throughout the steel cables and deck, "
                "engineers can monitor real-time vibrations and tension. This data allows for predictive "
                "maintenance, identifying microscopic cracks before they compromise structural integrity.\n\n"
                "Aerodynamics are a life-or-death priority in bridge design. Using advanced computational fluid "
                "dynamics (CFD), engineers shape the cross-section of the bridge to minimize 'vortex shedding.' "
                "By controlling how the wind flows over and under the deck, we prevent the destructive resonance "
                "oscillations that caused historical bridge collapses.\n\n"
                "Materials science is also evolving with the use of carbon fiber reinforced polymers (CFRP). "
                "These materials are corrosion-resistant, which is essential for maritime bridges exposed to salt "
                "spray. Replacing traditional steel rebar with CFRP can extend the lifespan of a bridge deck "
                "from 50 years to over 100 years with minimal intervention.\n\n"
                "Dynamic loading remains a complex challenge. Bridges must account for the synchronized rhythmic "
                "loading of traffic and pedestrians, as well as seismic activity. Tuned Mass Dampers (TMDs) "
                "are often installed inside the bridge pylons to absorb kinetic energy and stabilize the "
                "structure during high-wind events or tremors.\n\n"
                "Looking forward, modular construction is the next frontier. Prefabricated bridge sections "
                "can be 3D printed or cast in controlled factory environments and then shipped to the site. "
                "This reduces construction time by 40% and significantly lowers the safety risks associated "
                "with long-duration work over busy waterways or highways."
            )
        },
        {
            "title": "Seismic Retrofitting Techniques",
            "cat": eng,
            "image": "https://images.pexels.com/photos/2219024/pexels-photo-2219024.jpeg?auto=compress&cs=tinysrgb&w=1000",
            "content": (
                "Protecting the existing built environment from tectonic shifts is one of the most critical "
                "challenges in civil engineering. Seismic retrofitting involves modifying older structures "
                "to make them more resistant to ground motion through the addition of energy-dissipating "
                "components and structural reinforcements.\n\n"
                "One of the most effective methods is 'Base Isolation.' This involves placing flexible bearings "
                "made of lead and rubber between the building's foundation and its superstructure. During a "
                "seismic event, the isolators absorb the kinetic energy, allowing the ground to move while the "
                "building remains relatively stationary and undamaged.\n\n"
                "For high-rise structures, 'Fluid Viscous Dampers' are often used. These act like giant shock "
                "absorbers, converting seismic energy into heat. Installed in the diagonal bracing of a "
                "building, they significantly reduce the inter-story drift that causes glass windows to "
                "shatter and non-structural elements to fail during a quake.\n\n"
                "Another common technique involves 'Carbon Fiber Wraps' around concrete columns. Many older "
                "buildings have columns that lack sufficient confinement. Wrapping these in high-tensile carbon "
                "fabric prevents the concrete from spalling under intense axial pressure, keeping the "
                "gravity-load system intact during the shaking.\n\n"
                "Soil-structure interaction is also a major focus. Engineers use 'Jet Grouting' to strengthen "
                "the soil beneath a foundation, preventing liquefaction—a phenomenon where saturated soil "
                "behaves like a liquid. By injecting cement into the ground, they create a solid platform "
                "that prevents the building from sinking or tilting during a disaster.\n\n"
                "As we move forward, researchers are exploring 'Self-Centering' frames. These use "
                "shape-memory alloys that can stretch during an earthquake and then return to their "
                "original shape afterward. This allows a building to be occupied immediately after "
                "a major event, rather than being condemned due to permanent structural tilt."
            )
        }
    ]

    for p in posts:
        Blog.objects.create(
            title=p['title'], 
            slug=slugify(p['title']), 
            content=p['content'], 
            image_url=p['image'],
            author=user, 
            category=p['cat'], 
            status='published'
        )
    print(f"✅ Success! {Blog.objects.count()} technical deep-dives created.")

if __name__ == '__main__':
    seed()