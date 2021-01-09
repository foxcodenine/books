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
    },
    findEvent(dayId, details) {
        
        const objDay = this.state.seedData.find(day => day.id === dayId);
        const objEvent = objDay.events.find(event => event.details === details);
        return objEvent;
    },
    editEvent(dayId, details) {        

        const objEvent = this.findEvent(dayId, details);
        objEvent.edit = true;
    },

    updateEvent(dayId, details, newEventDetails) {

        const objEvent = this.findEvent(dayId, details);
        objEvent.details = newEventDetails;
        objEvent.edit = false;
    },
    resetAllEvent() {
        this.state.seedData.map(dayObj => {

            dayObj.events.map(eventObj => {
                eventObj.edit = false;
            });
        });        
    },
    deleteEvent(dayId, eventDetails) {

        const dayObj = this.state.seedData.find((day) => day.id == dayId);

        const eventIndex = dayObj.events.findIndex(event =>  event.details === eventDetails);

        dayObj.events.splice(eventIndex, 1);
    }
}

