import { seedData } from './seed.js'

export const store = {
    state: {
        seedData
    },
    getActiveDay() {
        
        return this.state.seedData.find((day) => day.active);
    },
    setActiveDay(id) {
        this.state.seedData.map(dayObj => {
            dayObj.id === id ? dayObj.active = true : dayObj.active = false;
        })
    },
    addEvent(eventDetails) {
        const activeDay = this.getActiveDay();
        activeDay.events.push({details: eventDetails, edit: false});
    }

}

console.log(store);